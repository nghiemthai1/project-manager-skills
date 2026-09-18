# MIT License
#
# Copyright (c) 2026 Thai Nghiem
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Render evidence-led RACI matrices to offline HTML, SVG, JSON and CSV.

Python 3.11+ standard library. The renderer audits explicit assignments; it
does not infer authority, confirm agreement, estimate capacity or rewrite RACI
letters.
"""
import argparse
import base64
import csv
import html
import io
import json
from pathlib import Path
import sys
import textwrap

CODES = ('R', 'A', 'C', 'I', 'A/R', '?', '—')
STATES = ('proposed', 'confirmed', 'disputed', 'unknown')
COLORS = {
    'R': ('#d9e8ff', '#173d73'), 'A': ('#f7d7e6', '#8c164c'),
    'C': ('#d7eee9', '#155d54'), 'I': ('#e9eef5', '#38475a'),
    'A/R': ('#eadcf7', '#59327d'), '?': ('#fff0d0', '#744c0e'),
    '—': ('#ffffff', '#5b6677'),
}


def esc(value):
    return html.escape(str(value), quote=True)


def _required_text(item, key, context):
    if not isinstance(item.get(key), str) or not item[key].strip():
        raise ValueError(f'{context} {key}: nonempty text required')


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('Expected a RACI snapshot object')
    for key in ('title', 'version', 'as_of', 'source', 'scope', 'state'):
        _required_text(data, key, 'snapshot')
    roles, rows = data.get('roles'), data.get('rows')
    if not isinstance(roles, list) or not roles:
        raise ValueError('roles must be a nonempty list')
    if not isinstance(rows, list) or not rows:
        raise ValueError('rows must be a nonempty list')
    role_ids = []
    for role in roles:
        if not isinstance(role, dict):
            raise ValueError('Each role must be an object')
        for key in ('id', 'label'):
            _required_text(role, key, 'role')
        for key in ('function', 'authority', 'source'):
            if key in role and not isinstance(role[key], str):
                raise ValueError(f'role {role["id"]} {key} must be text')
        role_ids.append(role['id'])
    if len(role_ids) != len(set(role_ids)):
        raise ValueError('Duplicate role ID')

    groups = data.get('row_groups', [])
    if not isinstance(groups, list):
        raise ValueError('row_groups must be a list')
    group_ids = set()
    for group in groups:
        if not isinstance(group, dict):
            raise ValueError('Each row group must be an object')
        for key in ('id', 'name', 'index'):
            _required_text(group, key, 'row group')
        if group['id'] in group_ids:
            raise ValueError('Duplicate row group ID')
        group_ids.add(group['id'])

    row_ids = []
    expected = set(role_ids)
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError('Each row must be an object')
        for key in ('id', 'label'):
            _required_text(row, key, 'row')
        if groups and row.get('group') not in group_ids:
            raise ValueError(f'{row["id"]}: group must reference row_groups')
        if 'source' in row and not isinstance(row['source'], str):
            raise ValueError(f'{row["id"]}: source must be text')
        if not isinstance(row.get('cells'), dict) or set(row['cells']) != expected:
            raise ValueError(f'{row["id"]}: every role needs an explicit cell, including unknowns')
        for role_id, cell in row['cells'].items():
            if not isinstance(cell, dict) or cell.get('code') not in CODES:
                raise ValueError(f'{row["id"]}/{role_id}: invalid code')
            if cell.get('state') not in STATES:
                raise ValueError(f'{row["id"]}/{role_id}: invalid confirmation state')
            for key in ('note', 'source'):
                if not isinstance(cell.get(key), str):
                    raise ValueError(f'{row["id"]}/{role_id}: {key} must be text')
            if cell['state'] == 'confirmed' and not cell['source'].strip():
                raise ValueError(f'{row["id"]}/{role_id}: confirmed requires an evidence reference')
        row_ids.append(row['id'])
    if len(row_ids) != len(set(row_ids)):
        raise ValueError('Duplicate row ID')

    presentation = data.get('presentation')
    if not isinstance(presentation, dict):
        raise ValueError('presentation is required')
    for key in ('eyebrow', 'headline', 'lede', 'insight_heading', 'decision'):
        _required_text(presentation, key, 'presentation')
    if presentation.get('default_row_id') not in set(row_ids):
        raise ValueError('default_row_id must reference a row')
    metrics = presentation.get('metrics')
    if not isinstance(metrics, list) or not metrics:
        raise ValueError('presentation metrics required')
    for metric in metrics:
        if not isinstance(metric, dict):
            raise ValueError('Each metric must be an object')
        for key in ('label', 'value', 'note'):
            _required_text(metric, key, 'metric')
    points = presentation.get('insight_points')
    if not isinstance(points, list) or any(not isinstance(point, str) or not point.strip() for point in points):
        raise ValueError('insight_points must be nonempty text entries')

    analysis = data.get('analysis')
    if not isinstance(analysis, dict):
        raise ValueError('analysis is required')
    _required_text(analysis, 'method', 'analysis')
    for key in ('consulted_review_threshold', 'accountability_concentration_threshold'):
        value = analysis.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f'analysis {key} must be a positive integer')
    if not isinstance(data.get('notes', []), list) or any(not isinstance(note, str) for note in data.get('notes', [])):
        raise ValueError('notes must be text entries')
    return data


def code_count(cells, code):
    if code in ('A', 'R'):
        return sum(cell['code'] in (code, 'A/R') for cell in cells)
    return sum(cell['code'] == code for cell in cells)


def audit(data):
    """Horizontal row audit. Findings describe review work and never mutate data."""
    findings = []
    threshold = data.get('analysis', {}).get('consulted_review_threshold', 4)
    for row in data['rows']:
        cells = list(row['cells'].values())
        accountable = code_count(cells, 'A')
        responsible = code_count(cells, 'R')
        consulted = code_count(cells, 'C')
        flags = []
        if accountable != 1:
            flags.append(f'{accountable} A assignments; confirm one bounded authority')
        if not responsible:
            flags.append('No R assignment')
        if any(cell['code'] == '?' for cell in cells):
            flags.append('Unresolved cells')
        if any(cell['state'] == 'disputed' for cell in cells):
            flags.append('Disputed assignment')
        if any(cell['code'] != '—' and cell['state'] != 'confirmed' for cell in cells):
            flags.append('Assignments not fully confirmed')
        if consulted > threshold:
            flags.append(f'{consulted} C assignments; verify consultation boundary')
        if flags:
            severity = 'critical' if accountable != 1 or not responsible or any(cell['state'] == 'disputed' for cell in cells) else 'review'
            findings.append({'id': row['id'], 'severity': severity, 'findings': flags})
    return findings


def role_audit(data):
    """Vertical role counts and transparent pattern signals, never workload."""
    threshold = data.get('analysis', {}).get('accountability_concentration_threshold', 3)
    result = []
    for role in data['roles']:
        cells = [row['cells'][role['id']] for row in data['rows']]
        counts = {code: code_count(cells, code) for code in ('A', 'R', 'C', 'I', '?')}
        counts['—'] = code_count(cells, '—')
        exact_counts = {code: sum(cell['code'] == code for cell in cells) for code in CODES}
        states = {state: sum(cell['state'] == state for cell in cells) for state in STATES}
        signals = []
        if counts['A'] >= threshold:
            signals.append(f'{counts["A"]} accountable rows meet the review threshold of {threshold}')
        if counts['?']:
            signals.append(f'{counts["?"]} unresolved assignment{"s" if counts["?"] != 1 else ""}')
        if states['disputed']:
            signals.append(f'{states["disputed"]} disputed assignment{"s" if states["disputed"] != 1 else ""}')
        if counts['I'] and not any(counts[code] for code in ('A', 'R', 'C')):
            signals.append('Informed-only pattern; confirm the role belongs in this matrix')
        if not signals:
            signals.append('No vertical review signal under the declared rules')
        result.append({'id': role['id'], 'label': role['label'], 'counts': counts, 'exact_counts': exact_counts,
                       'states': states, 'signals': signals})
    return result


def spreadsheet_text(value):
    text = '' if value is None else str(value)
    return "'" + text if isinstance(value, str) and text.startswith(('=', '+', '-', '@', '\t', '\r')) else text


def render_csv(data):
    validate(data)
    stream = io.StringIO(newline='')
    writer = csv.writer(stream, lineterminator='\n')
    writer.writerow(['row_group', 'row_id', 'deliverable', 'row_source', 'role_id', 'role', 'role_function',
                     'code', 'confirmation', 'work_boundary', 'assignment_source'])
    for row in data['rows']:
        for role in data['roles']:
            cell = row['cells'][role['id']]
            values = (row.get('group', ''), row['id'], row['label'], row.get('source', ''), role['id'],
                      role['label'], role.get('function', ''), cell['code'], cell['state'], cell['note'], cell['source'])
            writer.writerow([spreadsheet_text(value) for value in values])
    return stream.getvalue()


def _wrap(value, width):
    return textwrap.wrap(str(value), width=width, break_long_words=False, break_on_hyphens=False) or ['']


def _svg_text(x, y, value, size=13, fill='#13294b', weight='400', anchor=None, extra=''):
    anchor_attr = f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}"{anchor_attr}{extra}>{esc(value)}</text>'


def render_svg(data):
    validate(data)
    roles, rows = data['roles'], data['rows']
    findings = {item['id']: item for item in audit(data)}
    left, cell_width = 370, 155
    width = max(1400, left + cell_width * len(roles) + 34)
    row_height, group_height = 78, 40
    groups = data.get('row_groups') or [{'id': '', 'index': '01', 'name': 'Responsibility assignments'}]
    group_rows = [(group, [row for row in rows if row.get('group', '') == group['id']]) for group in groups]
    matrix_height = 72 + sum(group_height + len(items) * row_height for _, items in group_rows)
    graph_top = 296
    footer_top = graph_top + matrix_height + 34
    height = footer_top + 145
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{esc(data["title"])}</title>',
        f'<desc id="desc">Responsibility assignment matrix as of {esc(data["as_of"])}. Letters and confirmation state are distinct. Counts are not utilization.</desc>',
        '<defs><filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#0b1f40" flood-opacity=".11"/></filter></defs>',
        '<rect width="100%" height="100%" fill="#f5f7fb"/><rect x="0" y="0" width="12" height="100%" fill="#173b2d"/>',
        _svg_text(38, 44, data['presentation']['eyebrow'].upper(), 12, '#d80b61', '800', extra=' letter-spacing="2"'),
        _svg_text(38, 100, data['presentation']['headline'], 42, '#0c234b', '800'),
        _svg_text(38, 137, data['presentation']['lede'], 16, '#536581'),
    ]
    metric_x = 38
    for metric in data['presentation']['metrics'][:5]:
        out.extend([
            f'<g filter="url(#shadow)"><rect x="{metric_x}" y="168" width="226" height="91" rx="14" fill="#fff" stroke="#ccd6e5"/>',
            _svg_text(metric_x + 16, 194, metric['label'].upper(), 10, '#667085', '800', extra=' letter-spacing="1"'),
            _svg_text(metric_x + 16, 225, metric['value'], 23, '#0c234b', '800'),
            _svg_text(metric_x + 16, 246, metric['note'][:38], 10, '#667085'),
            '</g>',
        ])
        metric_x += 240
    out.append(f'<g transform="translate(22 {graph_top})"><rect width="{width-44}" height="{matrix_height}" rx="18" fill="#fff" stroke="#ccd6e5"/>')
    out.append(_svg_text(22, 30, 'DELIVERABLE / DECISION', 11, '#536581', '800', extra=' letter-spacing=".7"'))
    for index, role in enumerate(roles):
        x = left - 22 + index * cell_width + cell_width / 2
        for line_index, line in enumerate(_wrap(role['label'], 17)[:2]):
            out.append(_svg_text(x, 24 + line_index * 15, line, 11, '#0c234b', '700', 'middle'))
        out.append(_svg_text(x, 58, role.get('function', role['id'])[:18], 9, '#667085', '400', 'middle'))
    y = 72
    for group, items in group_rows:
        out.append(f'<rect x="0" y="{y}" width="{width-44}" height="{group_height}" fill="#edf2f8"/>')
        out.append(f'<rect x="18" y="{y+9}" width="30" height="22" rx="7" fill="#0c234b"/>')
        out.append(_svg_text(33, y + 25, group['index'], 10, '#fff', '800', 'middle'))
        out.append(_svg_text(60, y + 25, group['name'], 15, '#0c234b', '800'))
        y += group_height
        for row in items:
            out.append(f'<g data-row="{esc(row["id"])}"><rect x="0" y="{y}" width="{width-44}" height="{row_height}" fill="#fff" stroke="#dbe3ee"/>')
            out.append(f'<rect x="0" y="{y}" width="4" height="{row_height}" fill="{"#d80b61" if row["id"] in findings else "#08766c"}"/>')
            out.append(_svg_text(18, y + 23, row['id'], 10, '#d80b61', '800'))
            for line_index, line in enumerate(_wrap(row['label'], 39)[:2]):
                out.append(_svg_text(18, y + 43 + line_index * 16, line, 13, '#13294b', '700'))
            for index, role in enumerate(roles):
                cell = row['cells'][role['id']]
                background, foreground = COLORS[cell['code']]
                x = left - 22 + index * cell_width + 8
                stroke = '#b42318' if cell['state'] == 'disputed' else ('#d80b61' if cell['state'] == 'unknown' else '#b8c6d9')
                dash = '' if cell['state'] == 'confirmed' else ' stroke-dasharray="5 3"'
                out.append(f'<rect x="{x}" y="{y+11}" width="{cell_width-16}" height="{row_height-22}" rx="10" fill="{background}" stroke="{stroke}"{dash}/>')
                out.append(_svg_text(x + 12, y + 38, cell['code'], 19, foreground, '800'))
                out.append(_svg_text(x + 12, y + 55, cell['state'], 9, foreground, '600'))
            out.append('</g>')
            y += row_height
    out.append('</g>')
    out.append(_svg_text(38, footer_top, 'R performs  ·  A owns the result  ·  C is consulted  ·  I is informed  ·  ? unresolved  ·  — no assignment', 11, '#536581', '700'))
    out.append(_svg_text(38, footer_top + 25, 'Solid = confirmed  ·  dashed = proposed or unknown  ·  red outline = disputed. Letter and confirmation are separate dimensions.', 11, '#536581'))
    out.append(_svg_text(38, footer_top + 50, f'{len(rows)} rows · {len(roles)} roles · {len(findings)} rows with review findings. Counts indicate assignment patterns, not workload or capacity.', 11, '#536581'))
    out.append(_svg_text(38, footer_top + 75, f'As of {data["as_of"]} · {data["state"]} · Source: {data["source"][:150]}', 11, '#667085'))
    out.append(_svg_text(38, footer_top + 100, data['analysis']['method'][:185], 11, '#667085'))
    out.append('</svg>')
    return ''.join(out)


def _safe_json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')


def _data_uri(text, media_type):
    encoded = base64.b64encode(text.encode('utf-8')).decode('ascii')
    return f'data:{media_type};base64,{encoded}'


def render_html(data, svg=None, csv_text=None):
    validate(data)
    svg = svg or render_svg(data)
    csv_text = csv_text or render_csv(data)
    findings = audit(data)
    finding_map = {item['id']: item for item in findings}
    role_findings = role_audit(data)
    group_names = {group['id']: group['name'] for group in data.get('row_groups', [])}
    role_map = {role['id']: role for role in data['roles']}

    role_options = ''.join(f'<option value="{esc(role["id"])}">{esc(role["label"])}</option>' for role in data['roles'])
    group_options = ''.join(f'<option value="{esc(group["id"])}">{esc(group["name"])}</option>' for group in data.get('row_groups', []))
    headers = ''.join(
        f'<th scope="col" data-role="{esc(role["id"])}"><span>{esc(role["label"])}</span><small>{esc(role.get("function", role["id"]))}</small></th>'
        for role in data['roles']
    )
    matrix_rows, mobile_rows, audit_rows = [], [], []
    current_group = None
    for row in data['rows']:
        group = row.get('group', '')
        if group != current_group:
            current_group = group
            matrix_rows.append(
                f'<tr class="group-row" data-group-heading="{esc(group)}"><th colspan="{len(data["roles"])+1}">'
                f'<span>{esc(group_names.get(group, "Responsibility assignments"))}</span></th></tr>'
            )
        search = ' '.join([
            row['id'], row['label'], row.get('source', ''), group_names.get(group, ''),
            *[role['label'] + ' ' + json.dumps(row['cells'][role['id']], ensure_ascii=False) for role in data['roles']],
        ]).lower()
        states = ' '.join(sorted({cell['state'] for cell in row['cells'].values()}))
        authority = 'true' if any(cell['code'] in ('A', 'A/R') for cell in row['cells'].values()) else 'false'
        has_findings = str(row['id'] in finding_map).lower()
        cells, cards = [], []
        for role in data['roles']:
            cell = row['cells'][role['id']]
            detail_label = f'{row["id"]}: {row["label"]}; {role["label"]}; {cell["code"]}; {cell["state"]}'
            class_code = cell['code'].replace('/', '').replace('?', 'unknown').replace('—', 'none')
            cells.append(
                f'<td data-role="{esc(role["id"])}"><button class="cell code-{esc(class_code)}" '
                f'data-state="{esc(cell["state"])}" data-row-id="{esc(row["id"])}" data-role-id="{esc(role["id"])}" '
                f'data-detail="{esc(detail_label)}" aria-label="{esc(detail_label)}"><b>{esc(cell["code"])}</b>'
                f'<small>{esc(cell["state"])}</small></button></td>'
            )
            cards.append(
                f'<button class="card-cell" data-role="{esc(role["id"])}" data-state="{esc(cell["state"])}" '
                f'data-row-id="{esc(row["id"])}" data-role-id="{esc(role["id"])}" data-detail="{esc(detail_label)}">'
                f'<span>{esc(role["label"])}</span><strong>{esc(cell["code"])}</strong><small>{esc(cell["state"])}</small></button>'
            )
        attrs = (f'data-row="{esc(row["id"])}" data-group="{esc(group)}" data-findings="{has_findings}" '
                 f'data-states="{esc(states)}" data-authority="{authority}" data-search="{esc(search)}"')
        matrix_rows.append(f'<tr class="assignment-row" {attrs}><th scope="row"><small>{esc(row["id"])}</small><b>{esc(row["label"])}</b></th>{"".join(cells)}</tr>')
        mobile_rows.append(
            f'<article {attrs}><div class="card-kicker">{esc(group_names.get(group, "Assignments"))} · {esc(row["id"])}</div>'
            f'<h3>{esc(row["label"])}</h3><div class="card-cells">{"".join(cards)}</div></article>'
        )
        row_finding = finding_map.get(row['id'])
        finding_items = row_finding['findings'] if row_finding else ['No horizontal review signal under the declared rules']
        counts = {code: sum(cell['code'] == code for cell in row['cells'].values())
                  for code in ('A', 'R', 'A/R', 'C', 'I', '?')}
        audit_rows.append(
            f'<article class="audit-card {esc(row_finding["severity"] if row_finding else "clear")}" data-audit-row="{esc(row["id"])}" {attrs}>'
            f'<div><small>{esc(row["id"])} · {esc(group_names.get(group, "Assignments"))}</small><h3>{esc(row["label"])}</h3>'
            f'<ul>{"".join(f"<li>{esc(item)}</li>" for item in finding_items)}</ul></div>'
            f'<div class="audit-counts">{"".join(f"<span><b>{count}</b>{esc(code)}</span>" for code, count in counts.items())}</div></article>'
        )

    profile_cards = []
    max_rows = max(1, len(data['rows']))
    for summary in role_findings:
        role = role_map[summary['id']]
        segments = []
        for code, color in (('A', '#d80b61'), ('R', '#2f6fc2'), ('A/R', '#7f56a8'),
                            ('C', '#08766c'), ('I', '#7a879b'), ('?', '#b54708')):
            count = summary['exact_counts'][code]
            if count:
                segments.append(f'<span style="width:{count/max_rows*100:.2f}%;background:{color}" title="{esc(code)}: {count}"></span>')
        role_counts_html = ''.join(
            f'<span><b>{summary["exact_counts"][code]}</b>{esc(code)}</span>'
            for code in ('A', 'R', 'A/R', 'C', 'I', '?', '—')
        )
        profile_cards.append(
            f'<article class="role-card" data-role="{esc(role["id"])}"><div class="role-head"><div><small>{esc(role.get("function", "ROLE PROFILE"))}</small>'
            f'<h3>{esc(role["label"])}</h3></div><span class="role-total">{sum(summary["states"].values()) - summary["counts"]["—"]} assigned</span></div>'
            f'<div class="stack" aria-label="Assignment relationship counts">{"".join(segments)}</div>'
            f'<div class="role-counts">{role_counts_html}</div>'
            f'<p><b>Confirmation:</b> {summary["states"]["confirmed"]} confirmed · {summary["states"]["proposed"]} proposed · '
            f'{summary["states"]["disputed"]} disputed · {summary["states"]["unknown"]} unknown</p>'
            f'<ul>{"".join(f"<li>{esc(signal)}</li>" for signal in summary["signals"])}</ul>'
            f'<p class="boundary"><b>Authority boundary:</b> {esc(role.get("authority", "Not further specified"))}</p></article>'
        )

    json_text = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    export_links = ''.join([
        f'<a class="button" download="raci-matrix.svg" href="{_data_uri(svg, "image/svg+xml")}">Source SVG</a>',
        f'<a class="button" download="raci-matrix.json" href="{_data_uri(json_text, "application/json")}">Source JSON</a>',
        f'<a class="button" download="raci-matrix.csv" href="{_data_uri(csv_text, "text/csv")}">Source CSV</a>',
    ])
    payload = _safe_json(data)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(data['title'])}</title>
<style>
:root{{--navy:#0c234b;--ink:#13294b;--muted:#60708b;--line:#ccd6e5;--paper:#f5f7fb;--pink:#d80b61;--green:#08766c;--red:#b42318;--amber:#b54708}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--paper);color:var(--ink);font:15px/1.42 Inter,Segoe UI,Arial,sans-serif;border-left:10px solid #173b2d;overflow-wrap:anywhere}}button,input,select,textarea{{font:inherit}}button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,a:focus-visible,[tabindex]:focus-visible{{outline:3px solid #ff8fbd;outline-offset:2px}}.page{{padding:28px 20px 54px;max-width:1800px;margin:auto}}header{{display:flex;gap:32px;justify-content:space-between;align-items:end;margin-bottom:22px}}.eyebrow{{font-size:12px;letter-spacing:2px;color:var(--pink);font-weight:800}}h1{{font-size:46px;line-height:1.05;margin:14px 0 0}}.lede{{max-width:760px;text-align:right;color:var(--muted);font-size:18px}}.metrics{{display:grid;grid-template-columns:repeat(4,minmax(170px,1fr));gap:12px;margin-bottom:18px}}.metric,.toolbar,.workspace,.insight,.role-card{{background:#fff;border:1px solid var(--line);border-radius:18px}}.metric{{padding:14px 16px;min-height:104px}}.metric b{{display:block;font-size:24px;margin:4px 0}}.metric span,.metric small{{display:block;color:var(--muted)}}.metric span{{font-size:11px;font-weight:800;letter-spacing:.08em}}.toolbar{{padding:14px 16px;display:flex;gap:11px;align-items:end;flex-wrap:wrap;position:sticky;top:8px;z-index:8;box-shadow:0 8px 28px #0c234b12}}label{{font-size:10px;font-weight:800;color:#536581;letter-spacing:.06em}}label input,label select{{display:block;margin-top:5px;min-width:165px}}input,select,.button{{height:46px;border:1px solid #b9c8dc;border-radius:12px;background:#fff;padding:0 13px;color:var(--navy)}}.button{{display:inline-flex;align-items:center;justify-content:center;font-weight:750;cursor:pointer;text-decoration:none}}.button.active,.button[aria-pressed="true"]{{border-color:var(--pink);color:#a40048;background:#fff5fa;box-shadow:0 0 0 2px #ffd4e6 inset}}.button.dark{{background:var(--navy);color:#fff}}.button:disabled{{opacity:.45;cursor:not-allowed}}.spacer{{flex:1}}#scope{{margin:14px 0 0;padding:11px 15px;border-left:4px solid var(--pink);background:#fff7fb;color:#4f607a}}.workspace{{margin-top:16px;overflow:hidden}}.workspace-head{{display:flex;justify-content:space-between;gap:20px;padding:16px 18px;border-bottom:1px solid var(--line);align-items:center}}.workspace-head b{{font-size:18px}}.workspace-head span{{color:var(--muted)}}.tabs{{display:flex;gap:8px;flex-wrap:wrap}}.view{{display:none}}.view.active{{display:block}}.scroll{{overflow:auto;max-height:68vh;background:#fff}}table{{border-collapse:separate;border-spacing:0;min-width:980px;width:100%}}th,td{{border-right:1px solid #dbe3ee;border-bottom:1px solid #dbe3ee;padding:10px;text-align:left;vertical-align:middle}}thead th{{position:sticky;top:0;background:#edf2f8;z-index:4;min-width:142px;color:var(--navy)}}thead th:first-child{{left:0;z-index:6;min-width:310px}}thead th span,thead th small{{display:block}}thead th small{{font-weight:400;color:var(--muted);margin-top:3px}}tbody .assignment-row th{{position:sticky;left:0;background:#fff;z-index:3;min-width:310px;max-width:360px;border-left:4px solid #d80b61}}tbody .assignment-row th small,tbody .assignment-row th b{{display:block}}tbody .assignment-row th small{{color:var(--pink);margin-bottom:3px}}.group-row th{{position:sticky;left:0;background:#e8eef6;color:var(--navy);z-index:3;padding:12px 18px;font-size:16px}}.cell{{min-width:110px;width:100%;min-height:58px;text-align:left;border:1px dashed #9eacc0;border-radius:10px;padding:8px 10px;background:#fff;cursor:pointer}}.cell b{{display:block;font-size:20px}}.cell small{{display:block;text-transform:capitalize}}.cell[data-state="confirmed"]{{border-style:solid}}.cell[data-state="disputed"]{{border:2px solid var(--red)}}.cell[data-state="unknown"]{{border-color:var(--pink)}}.cell.selected{{box-shadow:0 0 0 3px #ff9ac4}}.cell.edited,.card-cell.edited{{box-shadow:0 0 0 3px #d80b61 inset}}.code-R{{background:#d9e8ff;color:#173d73}}.code-A{{background:#f7d7e6;color:#8c164c}}.code-C{{background:#d7eee9;color:#155d54}}.code-I{{background:#e9eef5;color:#38475a}}.code-AR{{background:#eadcf7;color:#59327d}}.code-unknown{{background:#fff0d0;color:#744c0e}}.code-none{{background:#fff;color:#5b6677}}.mobile{{display:none;padding:12px}}.mobile article{{border:1px solid var(--line);border-radius:14px;padding:15px;margin-bottom:12px;background:#fff}}.card-kicker{{font-size:10px;font-weight:800;color:var(--pink);letter-spacing:.06em}}.mobile h3{{margin:6px 0 12px}}.card-cells{{display:grid;gap:7px}}.card-cell{{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;text-align:left;min-height:48px;border:1px solid var(--line);border-radius:10px;background:#f9fbfd;padding:8px 10px;color:var(--ink)}}.card-cell strong{{font-size:18px}}.card-cell small{{color:var(--muted)}}.detail{{display:grid;grid-template-columns:1.1fr .9fr;gap:18px;padding:20px;border-top:1px solid var(--line);background:#fbfcfe}}.detail h2{{margin:4px 0 8px;font-size:23px}}.tag{{display:inline-block;padding:5px 9px;border-radius:99px;background:#eef2f7;font-size:11px;font-weight:800;margin:0 6px 5px 0}}.detail-facts{{display:grid;grid-template-columns:repeat(2,1fr);gap:9px}}.fact{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px}}.fact small{{display:block;color:var(--muted)}}.editor{{grid-column:1/-1;border:1px solid #f0a6c5;border-radius:14px;background:#fff7fb;padding:16px}}.editor-grid{{display:grid;grid-template-columns:150px 180px 1fr 1fr;gap:10px;align-items:end}}.editor label{{display:grid;gap:5px}}.editor input,.editor select,.editor textarea{{width:100%;min-width:0;border:1px solid #b9c8dc;border-radius:10px;background:#fff;color:var(--navy);padding:10px}}.editor textarea{{height:76px;resize:vertical}}.editor-actions{{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}}.edit-error{{color:var(--red);font-weight:700;margin:8px 0 0;min-height:21px}}.history{{border-top:1px solid var(--line);padding:0 20px 18px;background:#fbfcfe}}.history summary{{cursor:pointer;font-weight:800;padding:14px 0}}.history ol{{margin:0;padding-left:22px}}.history li{{margin:6px 0}}.audit-grid{{padding:18px;display:grid;grid-template-columns:repeat(2,minmax(300px,1fr));gap:12px}}.audit-card{{border:1px solid var(--line);border-left:5px solid var(--amber);border-radius:14px;padding:15px;display:grid;grid-template-columns:1fr auto;gap:14px;background:#fff}}.audit-card.critical{{border-left-color:var(--red)}}.audit-card.clear{{border-left-color:var(--green)}}.audit-card h3{{margin:4px 0}}.audit-card small{{color:var(--muted)}}.audit-card ul{{margin:8px 0 0;padding-left:18px}}.audit-counts,.role-counts{{display:flex;gap:6px;align-items:center;flex-wrap:wrap}}.audit-counts span,.role-counts span{{min-width:42px;text-align:center;background:#eef2f7;border-radius:9px;padding:6px;font-size:10px}}.audit-counts b,.role-counts b{{display:block;font-size:16px}}.roles-grid{{padding:18px;display:grid;grid-template-columns:repeat(2,minmax(300px,1fr));gap:14px;background:#f8fafc}}.role-card{{padding:17px}}.role-head{{display:flex;justify-content:space-between;gap:15px}}.role-head h3{{margin:3px 0 0}}.role-head small{{color:var(--pink);font-weight:800}}.role-total{{font-size:12px;font-weight:800;background:#edf2f8;border-radius:99px;padding:7px 10px;height:max-content}}.stack{{height:16px;border-radius:99px;display:flex;overflow:hidden;background:#edf2f7;margin:16px 0 10px}}.stack span{{display:block;height:100%;min-width:3px}}.role-card ul{{padding-left:18px}}.boundary{{border-left:4px solid var(--pink);padding:8px 10px;background:#fff7fb}}.insight{{margin-top:16px;padding:20px;display:grid;grid-template-columns:1fr 1fr;gap:28px}}.insight h2{{margin:4px 0}}.insight li{{margin:7px 0}}.decision{{border-left:5px solid var(--pink);padding:12px 14px;background:#fff5fa}}.legend{{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}}.legend span{{border:1px solid var(--line);border-radius:99px;padding:5px 9px;background:#fff;font-size:11px}}.empty{{padding:50px;text-align:center;color:var(--muted)}}.sr{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}}[hidden]{{display:none!important}}
@media(max-width:800px){{.page{{padding:18px 10px}}header{{display:block}}h1{{font-size:34px}}.lede{{text-align:left;margin-top:14px}}.metrics{{grid-template-columns:1fr 1fr}}.toolbar{{position:static}}label,label input,label select{{width:100%;min-width:0}}.spacer{{display:none}}.workspace-head{{display:block}}.tabs{{margin-top:12px}}.desktop{{display:none}}.mobile{{display:block}}.detail,.insight{{grid-template-columns:1fr}}.editor-grid{{grid-template-columns:1fr}}.audit-grid,.roles-grid{{grid-template-columns:1fr;padding:12px}}.audit-card{{grid-template-columns:1fr}}}}
@media print{{body{{border:0;background:#fff}}.page{{padding:0}}.toolbar{{position:static;box-shadow:none}}.toolbar label,.toolbar button,.toolbar a,.tabs,.editor,.history{{display:none!important}}#scope{{border:1px solid var(--line)}}.workspace,.metric,.insight{{break-inside:avoid}}.scroll{{max-height:none;overflow:visible}}thead th,tbody .assignment-row th,.group-row th{{position:static}}.mobile{{display:none}}.desktop{{display:block}}}}
</style></head><body><main class="page"><header><div><div class="eyebrow">{esc(data['presentation']['eyebrow'].upper())}</div><h1>{esc(data['presentation']['headline'])}</h1></div><div class="lede">{esc(data['presentation']['lede'])}</div></header>
<section class="metrics">{''.join(f'<div class="metric" data-metric="{esc(metric["label"].lower())}" data-source-note="{esc(metric["note"])}"><span>{esc(metric["label"])}</span><b>{esc(metric["value"])}</b><small>{esc(metric["note"])}</small></div>' for metric in data['presentation']['metrics'])}</section>
<section class="toolbar" aria-label="RACI controls"><label>FIND WORK<input id="search" type="search" placeholder="ID, deliverable, evidence"></label><label>WORKSTREAM<select id="group"><option value="">All workstreams</option>{group_options}</select></label><label>ROLE<select id="role"><option value="">All roles</option>{role_options}</select></label><label>CONFIRMATION<select id="state"><option value="">All states</option>{''.join(f'<option value="{state}">{state.title()}</option>' for state in STATES)}</select></label><label>REVIEW<select id="issues"><option value="all">All rows</option><option value="findings">Rows with findings</option></select></label><button class="button" id="authority" aria-pressed="false">Authority only</button><button class="button" id="reset">Reset view</button><button class="button" id="editToggle" aria-pressed="false">Edit draft</button><button class="button" id="undoEdit" disabled>Undo</button><button class="button" id="discardDraft" disabled>Restore source</button><span class="spacer"></span>{export_links}<button class="button" id="draftJson">Draft JSON</button><button class="button" id="draftCsv">Draft CSV</button><button class="button" id="visibleCsv">Visible draft CSV</button><button class="button dark" id="print">Print / PDF</button></section>
<p id="scope" aria-live="polite"></p>
<section class="workspace"><div class="workspace-head"><div><b>Responsibility control</b><br><span>Letters describe the relationship to work; confirmation describes evidence of agreement.</span></div><div class="tabs" role="tablist"><button class="button active" id="matrixTab" role="tab" aria-selected="true">Matrix</button><button class="button" id="auditTab" role="tab" aria-selected="false">Row audit</button><button class="button" id="rolesTab" role="tab" aria-selected="false">Role profiles</button></div></div>
<div class="view active" id="matrixView"><div class="desktop scroll"><table><caption class="sr">RACI assignments by deliverable and role</caption><thead><tr><th scope="col">Deliverable / decision</th>{headers}</tr></thead><tbody>{''.join(matrix_rows)}</tbody></table></div><div class="mobile">{''.join(mobile_rows)}</div><div class="empty" id="matrixEmpty" hidden>No rows match the current filters.</div></div>
<div class="view" id="auditView"><div class="audit-grid">{''.join(audit_rows)}</div><div class="empty" id="auditEmpty" hidden>No audit rows match the current filters.</div></div>
<div class="view" id="rolesView"><div class="roles-grid">{''.join(profile_cards)}</div></div>
<section class="detail" id="detail" aria-live="polite"><div><span class="tag">ASSIGNMENT DETAIL</span><h2 id="detail-title">Select an assignment</h2><p id="detail-text">Select a visible cell to inspect its bounded duty, confirmation state and evidence.</p></div><div class="detail-facts" id="detail-facts"><div class="fact"><small>Interpretation</small><b>A colored letter is not confirmation of agreement.</b></div></div><form class="editor" id="cellEditor" hidden><div class="editor-grid"><label>RELATIONSHIP<select id="editCode">{''.join(f'<option value="{esc(code)}">{esc(code)}</option>' for code in CODES)}</select></label><label>CONFIRMATION<select id="editState">{''.join(f'<option value="{esc(state)}">{esc(state.title())}</option>' for state in STATES)}</select></label><label>BOUNDED DUTY<textarea id="editNote" placeholder="What this role performs, owns, contributes, or receives"></textarea></label><label>EVIDENCE / SOURCE<textarea id="editSource" placeholder="Required when marking confirmed"></textarea></label></div><div class="editor-actions"><button class="button dark" id="saveCell" type="submit">Save local draft</button><button class="button" id="cancelEdit" type="button">Close editor</button></div><p class="edit-error" id="editError" aria-live="assertive"></p></form></section><details class="history" id="historyPanel"><summary>Local draft history (<span id="historyCount">0</span>)</summary><ol id="historyList"><li>No local edits yet.</li></ol></details></section>
<section class="insight"><div><div class="eyebrow">READOUT</div><h2>{esc(data['presentation']['insight_heading'])}</h2><ul>{''.join(f'<li>{esc(point)}</li>' for point in data['presentation']['insight_points'])}</ul><div class="legend"><span>R performs</span><span>A owns result</span><span>C consulted</span><span>I informed</span><span>? unresolved</span><span>— none</span></div></div><div><div class="decision">{esc(data['presentation']['decision'])}</div><p><b>Method boundary.</b> {esc(data['analysis']['method'])}</p><p><b>Snapshot.</b> {esc(data['state'])} · {esc(data['version'])} · As of {esc(data['as_of'])}</p><p><b>Source.</b> {esc(data['source'])}</p></div></section>
</main><script>
const SOURCE_DATA={payload},CODES=['R','A','C','I','A/R','?','—'],STATES=['proposed','confirmed','disputed','unknown'];let DATA=JSON.parse(JSON.stringify(SOURCE_DATA));const $=selector=>document.querySelector(selector),all=selector=>[...document.querySelectorAll(selector)];const STORAGE_KEY=`raci-local-draft:${{SOURCE_DATA.title}}:${{SOURCE_DATA.version}}:${{SOURCE_DATA.as_of}}`;let roles={{}},rows={{}},audit={{}},HISTORY=[],authorityOnly=false,view='matrix',selectedRow=DATA.presentation.default_row_id,selectedRole=DATA.roles[0].id,editMode=false,editMessage='';
const e=value=>String(value??'').replace(/[&<>"']/g,char=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[char]));const clone=value=>JSON.parse(JSON.stringify(value));const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);const groupName=row=>(DATA.row_groups||[]).find(group=>group.id===row.group)?.name||'Assignments';const codeClass=code=>'code-'+code.replace('/','').replace('?','unknown').replace('—','none');
function reindex(){{roles=Object.fromEntries(DATA.roles.map(role=>[role.id,role]));rows=Object.fromEntries(DATA.rows.map(row=>[row.id,row]));}}
function validCell(cell){{return cell&&CODES.includes(cell.code)&&STATES.includes(cell.state)&&typeof cell.note==='string'&&typeof cell.source==='string'&&!(cell.state==='confirmed'&&!cell.source.trim());}}
function loadDraft(){{try{{const saved=JSON.parse(localStorage.getItem(STORAGE_KEY)||'null');if(!saved||!saved.data||!Array.isArray(saved.history))return;const candidate=saved.data;if(candidate.rows?.map(row=>row.id).join('|')!==SOURCE_DATA.rows.map(row=>row.id).join('|')||candidate.roles?.map(role=>role.id).join('|')!==SOURCE_DATA.roles.map(role=>role.id).join('|'))return;for(const row of candidate.rows)for(const role of candidate.roles)if(!validCell(row.cells?.[role.id]))return;DATA=clone(SOURCE_DATA);candidate.rows.forEach((row,index)=>DATA.rows[index].cells=clone(row.cells));HISTORY=saved.history.slice(-200);}}catch(error){{console.warn('Local RACI draft could not be restored.',error);}}}}
function changedCells(){{let count=0;DATA.rows.forEach((row,rowIndex)=>DATA.roles.forEach(role=>{{if(!same(row.cells[role.id],SOURCE_DATA.rows[rowIndex].cells[role.id]))count++}}));return count;}}
function persist(){{try{{if(HISTORY.length)localStorage.setItem(STORAGE_KEY,JSON.stringify({{data:DATA,history:HISTORY}}));else localStorage.removeItem(STORAGE_KEY);}}catch(error){{console.warn('Local RACI draft could not be saved.',error);}}}}
function relationCount(cells,code){{return cells.filter(cell=>code==='A'||code==='R'?[code,'A/R'].includes(cell.code):cell.code===code).length;}}
function rowAudit(row){{const cells=Object.values(row.cells),a=relationCount(cells,'A'),r=relationCount(cells,'R'),c=relationCount(cells,'C'),findings=[];if(a!==1)findings.push(`${{a}} A assignments; confirm one bounded authority`);if(!r)findings.push('No R assignment');if(cells.some(cell=>cell.code==='?'))findings.push('Unresolved cells');if(cells.some(cell=>cell.state==='disputed'))findings.push('Disputed assignment');if(cells.some(cell=>cell.code!=='—'&&cell.state!=='confirmed'))findings.push('Assignments not fully confirmed');if(c>DATA.analysis.consulted_review_threshold)findings.push(`${{c}} C assignments; verify consultation boundary`);return findings.length?{{id:row.id,severity:a!==1||!r||cells.some(cell=>cell.state==='disputed')?'critical':'review',findings}}:null;}}
function roleSummary(role){{const cells=DATA.rows.map(row=>row.cells[role.id]),exact=Object.fromEntries(CODES.map(code=>[code,cells.filter(cell=>cell.code===code).length])),states=Object.fromEntries(STATES.map(state=>[state,cells.filter(cell=>cell.state===state).length])),counts={{A:relationCount(cells,'A'),R:relationCount(cells,'R'),C:exact.C,I:exact.I,'?':exact['?'],'—':exact['—']}},signals=[];if(counts.A>=DATA.analysis.accountability_concentration_threshold)signals.push(`${{counts.A}} accountable rows meet the review threshold of ${{DATA.analysis.accountability_concentration_threshold}}`);if(counts['?'])signals.push(`${{counts['?']}} unresolved assignment${{counts['?']===1?'':'s'}}`);if(states.disputed)signals.push(`${{states.disputed}} disputed assignment${{states.disputed===1?'':'s'}}`);if(counts.I&&!['A','R','C'].some(code=>counts[code]))signals.push('Informed-only pattern; confirm the role belongs in this matrix');if(!signals.length)signals.push('No vertical review signal under the declared rules');return{{exact,states,counts,signals}};}}
function renderAudit(){{audit={{}};const html=DATA.rows.map(row=>{{const finding=rowAudit(row);if(finding)audit[row.id]=finding;const items=finding?finding.findings:['No horizontal review signal under the declared rules'],counts=Object.fromEntries(['A','R','A/R','C','I','?'].map(code=>[code,Object.values(row.cells).filter(cell=>cell.code===code).length]));return`<article class="audit-card ${{e(finding?.severity||'clear')}}" data-audit-row="${{e(row.id)}}" data-row="${{e(row.id)}}"><div><small>${{e(row.id)}} · ${{e(groupName(row))}}</small><h3>${{e(row.label)}}</h3><ul>${{items.map(item=>`<li>${{e(item)}}</li>`).join('')}}</ul></div><div class="audit-counts">${{Object.entries(counts).map(([code,count])=>`<span><b>${{count}}</b>${{e(code)}}</span>`).join('')}}</div></article>`}}).join('');$('#auditView .audit-grid').innerHTML=html;}}
function renderRoles(){{const colors={{A:'#d80b61',R:'#2f6fc2','A/R':'#7f56a8',C:'#08766c',I:'#7a879b','?':'#b54708'}},total=Math.max(1,DATA.rows.length);$('#rolesView .roles-grid').innerHTML=DATA.roles.map(role=>{{const summary=roleSummary(role),segments=['A','R','A/R','C','I','?'].filter(code=>summary.exact[code]).map(code=>`<span style="width:${{summary.exact[code]/total*100}}%;background:${{colors[code]}}" title="${{e(code)}}: ${{summary.exact[code]}}"></span>`).join(''),assigned=DATA.rows.filter(row=>row.cells[role.id].code!=='—').length;return`<article class="role-card" data-role="${{e(role.id)}}"><div class="role-head"><div><small>${{e(role.function||'ROLE PROFILE')}}</small><h3>${{e(role.label)}}</h3></div><span class="role-total">${{assigned}} assigned</span></div><div class="stack" aria-label="Assignment relationship counts">${{segments}}</div><div class="role-counts">${{CODES.map(code=>`<span><b>${{summary.exact[code]}}</b>${{e(code)}}</span>`).join('')}}</div><p><b>Confirmation:</b> ${{summary.states.confirmed}} confirmed · ${{summary.states.proposed}} proposed · ${{summary.states.disputed}} disputed · ${{summary.states.unknown}} unknown</p><ul>${{summary.signals.map(signal=>`<li>${{e(signal)}}</li>`).join('')}}</ul><p class="boundary"><b>Authority boundary:</b> ${{e(role.authority||'Not further specified')}}</p></article>`}}).join('');}}
function syncCell(rowId,roleId){{const row=rows[rowId],role=roles[roleId],cell=row.cells[roleId],sourceRow=SOURCE_DATA.rows.find(item=>item.id===rowId),edited=!same(cell,sourceRow.cells[roleId]),label=`${{row.id}}: ${{row.label}}; ${{role.label}}; ${{cell.code}}; ${{cell.state}}`;all('[data-detail]').filter(button=>button.dataset.rowId===rowId&&button.dataset.roleId===roleId).forEach(button=>{{[...button.classList].filter(name=>name.startsWith('code-')).forEach(name=>button.classList.remove(name));button.classList.add(codeClass(cell.code));button.classList.toggle('edited',edited);button.dataset.state=cell.state;button.dataset.detail=label;button.setAttribute('aria-label',label+(edited?'; locally edited':''));button.title=edited?'Locally edited draft cell':'';const code=button.querySelector('b,strong'),state=button.querySelector('small');if(code)code.textContent=cell.code;if(state)state.textContent=cell.state;}});}}
function refreshRowMeta(){{DATA.rows.forEach(row=>{{const finding=rowAudit(row),search=[row.id,row.label,row.source||'',groupName(row),...DATA.roles.map(role=>role.label+' '+JSON.stringify(row.cells[role.id]))].join(' ').toLowerCase(),states=[...new Set(Object.values(row.cells).map(cell=>cell.state))].sort().join(' '),authority=Object.values(row.cells).some(cell=>['A','A/R'].includes(cell.code));all('.assignment-row,.mobile [data-row],.audit-card').filter(element=>(element.dataset.row||element.dataset.auditRow)===row.id).forEach(element=>{{element.dataset.group=row.group||'';element.dataset.findings=String(Boolean(finding));element.dataset.states=states;element.dataset.authority=String(authority);element.dataset.search=search;}});}});}}
function refreshMetrics(){{const cells=DATA.rows.flatMap(row=>Object.values(row.cells)),values={{'bounded rows':DATA.rows.length,'rows':DATA.rows.length,'named roles':DATA.roles.length,'roles':DATA.roles.length,'unresolved cells':cells.filter(cell=>cell.code==='?'||cell.state==='unknown').length,'unresolved':cells.filter(cell=>cell.code==='?'||cell.state==='unknown').length,'confirmed cells':cells.filter(cell=>cell.state==='confirmed').length,'confirmed':cells.filter(cell=>cell.state==='confirmed').length}},edits=changedCells();all('[data-metric]').forEach(card=>{{if(Object.hasOwn(values,card.dataset.metric))card.querySelector('b').textContent=values[card.dataset.metric];card.querySelector('small').textContent=edits&&['unresolved cells','unresolved','confirmed cells','confirmed'].includes(card.dataset.metric)?'Current local draft; source unchanged':card.dataset.sourceNote;}});}}
function renderHistory(){{$('#historyCount').textContent=HISTORY.length;$('#historyList').innerHTML=HISTORY.length?HISTORY.slice().reverse().map(change=>`<li><b>${{e(change.rowId)}} / ${{e(roles[change.roleId]?.label||change.roleId)}}</b>: ${{e(change.before.code)}} (${{e(change.before.state)}}) → ${{e(change.after.code)}} (${{e(change.after.state)}}) · ${{e(change.at)}}</li>`).join(''):'<li>No local edits yet.</li>';$('#undoEdit').disabled=!HISTORY.length;$('#discardDraft').disabled=!HISTORY.length&&!changedCells();$('#editToggle').setAttribute('aria-pressed',String(editMode));$('#editToggle').textContent=editMode?'Editing local draft':'Edit draft';document.body.classList.toggle('editing',editMode);}}
function renderDetail(rowId,roleId){{const row=rows[rowId],role=roles[roleId];if(!row||!role)return;const cell=row.cells[roleId],finding=audit[rowId],hiddenRole=$('#role').value&&$('#role').value!==roleId,sourceRow=SOURCE_DATA.rows.find(item=>item.id===rowId),edited=!same(cell,sourceRow.cells[roleId]);selectedRow=rowId;selectedRole=roleId;all('.cell,.card-cell').forEach(button=>button.classList.toggle('selected',button.dataset.rowId===rowId&&button.dataset.roleId===roleId));$('#detail-title').textContent=`${{row.id}} · ${{row.label}}`;$('#detail-text').textContent=`${{role.label}} is ${{cell.code}} (${{cell.state}}). Duty: ${{cell.note||'not further specified'}}. Evidence: ${{cell.source||'not supplied'}}.${{edited?' This cell differs from the source snapshot.':''}}${{hiddenRole?' This role is outside the current role focus.':''}}`;$('#detail-facts').innerHTML=`<div class="fact"><small>Role</small><b>${{e(role.label)}}</b></div><div class="fact"><small>Relationship</small><b>${{e(cell.code)}}</b></div><div class="fact"><small>Confirmation</small><b>${{e(cell.state)}}</b></div><div class="fact"><small>Workstream</small><b>${{e(groupName(row))}}</b></div><div class="fact"><small>Role authority</small><b>${{e(role.authority||'Not further specified')}}</b></div><div class="fact"><small>Row audit</small><b>${{e(finding?finding.findings.join('; '):'No signal under declared rules')}}</b></div>`;$('#cellEditor').hidden=!editMode;if(editMode){{$('#editCode').value=cell.code;$('#editState').value=cell.state;$('#editNote').value=cell.note;$('#editSource').value=cell.source;}}$('#editError').textContent=editMessage;}}
function rowVisible(element){{const row=rows[element.dataset.row||element.dataset.auditRow],q=$('#search').value.trim().toLowerCase(),group=$('#group').value,role=$('#role').value,state=$('#state').value,issues=$('#issues').value,roleCell=role?row.cells[role]:null;return(!q||element.dataset.search.includes(q))&&(!group||element.dataset.group===group)&&(!state||(roleCell?roleCell.state===state:Object.values(row.cells).some(cell=>cell.state===state)))&&(issues!=='findings'||element.dataset.findings==='true')&&(!authorityOnly||(roleCell?['A','A/R'].includes(roleCell.code):element.dataset.authority==='true'));}}
function update(){{let visible=0;all('.assignment-row').forEach(element=>{{const show=rowVisible(element);element.hidden=!show;if(show)visible++}});all('.mobile [data-row],.audit-card').forEach(element=>element.hidden=!rowVisible(element));all('.group-row').forEach(group=>{{const next=[];let sibling=group.nextElementSibling;while(sibling&&!sibling.classList.contains('group-row')){{if(sibling.matches('.assignment-row'))next.push(sibling);sibling=sibling.nextElementSibling}}group.hidden=!next.some(row=>!row.hidden)}});const focus=$('#role').value;all('[data-role]').forEach(element=>element.hidden=Boolean(focus)&&element.dataset.role!==focus);const qualifier=focus?' Role-focused view: assignments in other columns are hidden; return to All roles before auditing whole-row ownership.':' All roles shown.',filters=[];if(authorityOnly)filters.push('authority-only');if($('#state').value)filters.push($('#state').value);if($('#issues').value==='findings')filters.push('findings-only');const edits=changedCells();$('#scope').textContent=`${{visible}} / ${{DATA.rows.length}} rows shown.${{qualifier}}${{filters.length?' Active: '+filters.join(', ')+'.':''}} ${{edits?edits+' locally edited cell'+(edits===1?'':'s')+'; source exports remain unchanged.':'No local draft changes.'}} Filters affect inspection and Visible draft CSV only.`;$('#matrixEmpty').hidden=visible!==0;$('#auditEmpty').hidden=visible!==0;renderDetail(selectedRow,selectedRole);}}
function refreshAll(){{reindex();DATA.rows.forEach(row=>DATA.roles.forEach(role=>syncCell(row.id,role.id)));renderAudit();renderRoles();refreshRowMeta();refreshMetrics();renderHistory();update();}}
function setView(next){{view=next;[['matrix','matrixTab','matrixView'],['audit','auditTab','auditView'],['roles','rolesTab','rolesView']].forEach(([name,tab,panel])=>{{$('#'+tab).classList.toggle('active',name===view);$('#'+tab).setAttribute('aria-selected',String(name===view));$('#'+panel).classList.toggle('active',name===view)}});}}
function resetView(){{$('#search').value='';$('#group').value='';$('#role').value='';$('#state').value='';$('#issues').value='all';authorityOnly=false;$('#authority').setAttribute('aria-pressed','false');selectedRow=DATA.presentation.default_row_id;selectedRole=DATA.roles[0].id;editMessage='';update();}}
function csvSafe(value){{let text=String(value??''),unsafe=['=','+','-','@',String.fromCharCode(9),String.fromCharCode(13)];if(unsafe.includes(text[0]))text="'"+text;return '"'+text.replaceAll('"','""')+'"';}}
function csvText(rowSet=DATA.rows,roleSet=DATA.roles){{const lines=[['row_group','row_id','deliverable','row_source','role_id','role','role_function','code','confirmation','work_boundary','assignment_source'].map(csvSafe).join(',')];rowSet.forEach(row=>roleSet.forEach(role=>{{const cell=row.cells[role.id];lines.push([row.group||'',row.id,row.label,row.source||'',role.id,role.label,role.function||'',cell.code,cell.state,cell.note,cell.source].map(csvSafe).join(','))}}));return lines.join('\\n')+'\\n';}}
function download(name,body,type){{const href=URL.createObjectURL(new Blob([body],{{type}})),link=document.createElement('a');link.href=href;link.download=name;link.click();setTimeout(()=>URL.revokeObjectURL(href),0);}}
function draftSnapshot(){{const snapshot=clone(DATA);snapshot.state=`Local draft derived from: ${{SOURCE_DATA.state}}`;snapshot.local_draft={{base_version:SOURCE_DATA.version,base_as_of:SOURCE_DATA.as_of,exported_at:new Date().toISOString(),changed_cells:changedCells(),history:clone(HISTORY)}};return snapshot;}}
function exportVisible(){{const shown=new Set(all('.assignment-row:not([hidden])').map(element=>element.dataset.row)),focus=$('#role').value,rowSet=DATA.rows.filter(row=>shown.has(row.id)),roleSet=DATA.roles.filter(role=>!focus||role.id===focus);download('raci-matrix-visible-draft.csv',csvText(rowSet,roleSet),'text/csv');}}
function selectCell(button){{editMessage='';renderDetail(button.dataset.rowId,button.dataset.roleId);if(editMode)$('#editCode').focus();}}
all('[data-detail]').forEach(button=>{{button.addEventListener('click',()=>selectCell(button));button.addEventListener('keydown',event=>{{if(!['ArrowDown','ArrowUp','ArrowLeft','ArrowRight'].includes(event.key))return;event.preventDefault();const visible=all('.cell:not([hidden]),.card-cell:not([hidden])').filter(item=>item.offsetParent!==null),index=visible.indexOf(button),step=['ArrowDown','ArrowRight'].includes(event.key)?1:-1;visible[(index+step+visible.length)%visible.length]?.focus()}})}});
$('#cellEditor').addEventListener('submit',event=>{{event.preventDefault();const row=rows[selectedRow],before=clone(row.cells[selectedRole]),after={{code:$('#editCode').value,state:$('#editState').value,note:$('#editNote').value.trim(),source:$('#editSource').value.trim()}};if(!validCell(after)){{editMessage=after.state==='confirmed'&&!after.source?'Confirmed assignments require an evidence or source reference.':'The edited cell is invalid.';$('#editError').textContent=editMessage;return}}if(same(before,after)){{editMessage='No changes to save.';$('#editError').textContent=editMessage;return}}row.cells[selectedRole]=after;HISTORY.push({{rowId:selectedRow,roleId:selectedRole,before,after:clone(after),at:new Date().toISOString()}});editMessage='Local draft saved. The source snapshot and source exports are unchanged.';persist();refreshAll();}});
$('#editCode').addEventListener('change',()=>{{const current=rows[selectedRow].cells[selectedRole];if(current.state==='confirmed'&&$('#editCode').value!==current.code){{$('#editState').value='proposed';editMessage='Relationship changed; confirmation was reset to proposed. Select confirmed again only with current evidence.';$('#editError').textContent=editMessage;}}}});
$('#editState').addEventListener('change',()=>{{editMessage=$('#editState').value==='confirmed'&&!$('#editSource').value.trim()?'Add an evidence/source reference before saving a confirmed assignment.':'';$('#editError').textContent=editMessage;}});
$('#editToggle').onclick=()=>{{editMode=!editMode;editMessage=editMode?'Editing is local to this browser. Select a matrix cell, then save the draft fields below.':'';renderHistory();renderDetail(selectedRow,selectedRole);if(editMode)$('#editCode').focus();}};
$('#cancelEdit').onclick=()=>{{editMode=false;editMessage='';renderHistory();renderDetail(selectedRow,selectedRole);}};
$('#undoEdit').onclick=()=>{{const change=HISTORY.pop();if(!change)return;rows[change.rowId].cells[change.roleId]=clone(change.before);editMessage=`Undid the last local change to ${{change.rowId}} / ${{roles[change.roleId].label}}.`;persist();refreshAll();}};
$('#discardDraft').onclick=()=>{{if(!confirm('Restore every cell to the embedded source snapshot and clear local draft history?'))return;DATA=clone(SOURCE_DATA);HISTORY=[];selectedRow=DATA.presentation.default_row_id;selectedRole=DATA.roles[0].id;editMessage='Source snapshot restored; local draft history cleared.';persist();refreshAll();}};
$('#draftJson').onclick=()=>download('raci-matrix-local-draft.json',JSON.stringify(draftSnapshot(),null,2)+'\\n','application/json');$('#draftCsv').onclick=()=>download('raci-matrix-local-draft.csv',csvText(),'text/csv');$('#visibleCsv').onclick=exportVisible;$('#search').addEventListener('input',update);['group','role','state','issues'].forEach(id=>$('#'+id).addEventListener('change',update));$('#authority').onclick=()=>{{authorityOnly=!authorityOnly;$('#authority').setAttribute('aria-pressed',String(authorityOnly));update()}};$('#reset').onclick=resetView;$('#matrixTab').onclick=()=>setView('matrix');$('#auditTab').onclick=()=>setView('audit');$('#rolesTab').onclick=()=>setView('roles');$('#print').onclick=()=>window.print();document.addEventListener('keydown',event=>{{if(event.key==='Escape'){{if(editMode){{editMode=false;editMessage='';renderHistory();renderDetail(selectedRow,selectedRole)}}else resetView()}}}});
loadDraft();reindex();setView('matrix');refreshAll();
</script></body></html>'''


def demo():
    return validate({
        'title': 'Fictional RACI demonstration', 'version': 'draft-1', 'as_of': 'unknown',
        'source': 'Fictional built-in example', 'scope': 'One bounded handoff; assignments are proposals',
        'state': 'Proposed', 'roles': [
            {'id': 'PM', 'label': 'Project manager', 'function': 'coordination',
             'authority': 'Prepares the handover record; acceptance authority not claimed', 'source': 'Demo'},
            {'id': 'OPS', 'label': 'Service owner', 'function': 'operations',
             'authority': 'Acceptance authority unresolved', 'source': 'Demo'},
        ], 'row_groups': [{'id': 'handover', 'index': '01', 'name': 'Handover'}], 'rows': [{
            'id': 'H-1', 'label': 'Service transfer decision', 'group': 'handover', 'source': 'Demo',
            'cells': {
                'PM': {'code': 'R', 'state': 'proposed', 'note': 'Prepare the handover record', 'source': ''},
                'OPS': {'code': '?', 'state': 'unknown', 'note': 'Actual acceptance authority unresolved', 'source': ''},
            },
        }], 'presentation': {
            'eyebrow': 'Responsibility baseline', 'headline': 'Authority before initials',
            'lede': 'Inspect the assignment, its confirmation state and the evidence that supports it.',
            'default_row_id': 'H-1', 'metrics': [
                {'label': 'Rows', 'value': '1', 'note': 'One bounded decision'},
                {'label': 'Roles', 'value': '2', 'note': 'Named participants'},
                {'label': 'Unresolved', 'value': '1', 'note': 'Authority retained as unknown'},
                {'label': 'Confirmed', 'value': '0', 'note': 'No agreement inferred'},
            ], 'insight_heading': 'Resolve the acceptance boundary',
            'insight_points': ['The PM can prepare the record without owning acceptance.',
                               'The question mark is a control, not a blank.'],
            'decision': 'Confirm the service acceptance authority before treating the handover row as governed.',
        }, 'analysis': {
            'method': 'Rule-based horizontal and vertical review of supplied RACI cells; counts are not capacity.',
            'consulted_review_threshold': 4, 'accountability_concentration_threshold': 3,
        }, 'notes': ['This demonstration records no actual transfer or accepted assignment.'],
    })


def main(argv=None):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?', type=Path)
    parser.add_argument('--output', type=Path, help='Output filename stem; writes .svg/.html/.json/.csv')
    parser.add_argument('--demo', action='store_true')
    args = parser.parse_args(argv)
    try:
        if args.demo == bool(args.input):
            raise ValueError('Provide exactly one input JSON or --demo')
        data = demo() if args.demo else validate(json.loads(args.input.read_text(encoding='utf-8')))
        svg, csv_text = render_svg(data), render_csv(data)
        if not args.output:
            print(svg)
            return 0
        stem = args.output
        stem.parent.mkdir(parents=True, exist_ok=True)
        files = {
            '.svg': svg,
            '.html': render_html(data, svg, csv_text),
            '.json': json.dumps(data, indent=2, ensure_ascii=False) + '\n',
            '.csv': csv_text,
        }
        for suffix, content in files.items():
            Path(str(stem) + suffix).write_text(content, encoding='utf-8', newline='')
        print(json.dumps({
            'files': [str(stem) + suffix for suffix in files],
            'rows': len(data['rows']), 'roles': len(data['roles']),
            'row_findings': audit(data), 'role_profiles': role_audit(data),
        }, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print(f'Input error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
