# Northstar: split a blocker from an enhancement

Fictional additional message from Beck on 6 November 2026: "Some attachments have lost links in the export. Can your team patch the mapping today and add historical analytics while you're there?" Jules requests triage only. The canonical loss of links is MI-002; historical analytics is excluded from B1.

## Read of the request

| Lens | Evidence | Interpretation / unknown |
|---|---|---|
| Sender | Beck, vendor contact | Delivery contact, not internal acceptance or change authority |
| Literal ask | Patch mapping today; add analytics | Two materially different requests |
| Outcome | Restore usable attachment relationships | Supported by reported failure; exact affected population unknown |
| Additional outcome | Historical analytics | Motivation and success criteria unstated |
| Timing | Today requested | No evidence of available capacity or feasible repair duration |
| Requirements | Agreed attachments belong to migration scope | Need failure sample and expected mapping for repair verification |
| Authority | Jules coordinates, Saira business acceptance | Neither the message nor vendor contact approves added scope |

## Routes

1. **MI-002 delivery issue:** retain the failure evidence, identify affected records and obtain an accountable repair/verification plan. Establish whether the vendor or internal team owns the defect before assigning a patch. If an actual live-service incident exists, use its incident process; this message alone does not establish one.
2. **Historical analytics change:** record separately as a request outside the current boundary. Do not bundle it into mandatory defect repair. Clarify outcome and impacts before presenting an option to Noel.
3. **Investigation if failure extent is unknown:** inspect a bounded sample and preserve evidence of what is and is not affected. The sampling plan and owner require definition; a clean small sample would not prove all attachments correct.

No reply is drafted because Jules requested analysis only. The material follow-up is to obtain the failing export version, samples and expected mapping. A promise to patch today would invent capacity and technical ownership. The next artifact is an issue/action record plus a separate proposed change, not an approved combined task.

**Repair:** "One vendor ask equals one ticket" hides the excluded enhancement inside a legitimate blocker. Split the decisions and keep their evidence and authority distinct.
