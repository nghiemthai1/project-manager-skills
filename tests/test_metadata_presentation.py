"""Protect the flat GitHub authoring layout and its native list values."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('library_validator', ROOT/'scripts/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class MetadataPresentationTests(unittest.TestCase):
    def test_all_authored_headers_are_flat_with_real_lists(self):
        for path in (ROOT/'skills').glob('*/SKILL.md'):
            data, _ = validator.frontmatter(path.read_text(encoding='utf-8'))
            self.assertEqual(validator.metadata_errors(data), [], path.parent.name)
            self.assertIsInstance(data['best_for'], list)
            self.assertIsInstance(data['scenarios'], list)

    def test_nested_table_and_string_encoded_lists_are_rejected(self):
        data, _ = validator.frontmatter((ROOT/'skills/raci-matrix/SKILL.md').read_text(encoding='utf-8'))
        data['metadata'] = {'type':data['type']}
        data['best_for'] = '["An encoded list"]'
        messages = validator.metadata_errors(data)
        self.assertTrue(any('nested metadata' in message for message in messages))
        self.assertTrue(any('best_for' in message and 'YAML list' in message for message in messages))


if __name__ == '__main__': unittest.main()
