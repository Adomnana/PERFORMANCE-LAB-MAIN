import sys

#!/usr/bin/env python3
"""
Task 3 - Fill values into test structure.

Usage:
    python task3.py values.json tests.json report.json

values.json contains test results (various plausible structures).
tests.json contains nested objects where dicts with an "id" key should
receive a "value" field filled from values.json. The filled structure
is written to report.json.
"""

import json
from typing import Any, Dict

def build_values_map(obj: Any, mapping: Dict[str, Any]):
    """
    Recursively extract id->value entries from values.json. Accepts:
    - dict that maps id->value
    - list of {'id':.., 'value':..} entries
    - nested structures containing such entries
    """
    if isinstance(obj, dict):
        if 'id' in obj and 'value' in obj:
            mapping[str(obj['id'])] = obj['value']
            return mapping
        # if values are primitives, treat as direct map
        simple = True
        for v in obj.values():
            if isinstance(v, (dict, list)):
                simple = False
                break
        if simple:
            for k, v in obj.items():
                mapping[str(k)] = v
            return mapping
        # otherwise recurse
        for v in obj.values():
            build_values_map(v, mapping)
    elif isinstance(obj, list):
        for it in obj:
            build_values_map(it, mapping)
    return mapping

def fill_values_in_tests(obj: Any, mapping: Dict[str, Any]):
    """
    Recursively traverse tests.json. For any dict that has an 'id', set its
    'value' to mapping[id] if present (otherwise keep existing or null).
    """
    if isinstance(obj, dict):
        new = {}
        for k, v in obj.items():
            new[k] = fill_values_in_tests(v, mapping)
        if 'id' in obj:
            id_str = str(obj['id'])
            # prefer mapping value if present; else keep existing value or None
            new['value'] = mapping.get(id_str, obj.get('value', None))
        return new
    elif isinstance(obj, list):
        return [fill_values_in_tests(item, mapping) for item in obj]
    else:
        return obj

def main(argv):
    if len(argv) != 3:
        print("Usage: python task3.py values.json tests.json report.json", file=sys.stderr)
        return 2
    values_path, tests_path, report_path = argv[0], argv[1], argv[2]
    try:
        with open(values_path, "r", encoding="utf-8") as f:
            values_obj = json.load(f)
        with open(tests_path, "r", encoding="utf-8") as f:
            tests_obj = json.load(f)
    except Exception as e:
        print("Error reading input files:", e, file=sys.stderr)
        return 2

    mapping = build_values_map(values_obj, {})
    report_obj = fill_values_in_tests(tests_obj, mapping)

    try:
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report_obj, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Error writing report file:", e, file=sys.stderr)
        return 2

    print(f"Wrote report to {report_path}")
    return 0

if __name__ == "_main_":
    sys.exit(main(sys.argv[1:]))