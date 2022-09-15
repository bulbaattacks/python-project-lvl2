from collections import defaultdict


def build_diff_for_key(d1, d2, key):
    if key not in d1:
        return {
            "action": "record added",
            "value": d2.get(key)
        }
    if key not in d2:
        return {
            "action": "record deleted",
            "value": d1.get(key)
        }
    if isinstance(d1[key], dict) and isinstance(d2[key], dict):
        return {
            "action": "record nested",
            'children': diff_builder(d1[key], d2[key])
        }
    if d1.get(key) != d2.get(key):
        return {
            "action": "record changed",
            "previous": d1.get(key),
            "current": d2.get(key)
        }

    return {
        "action": "record is the same",
        "value": d1.get(key)
    }


def diff_builder(d1, d2):
    all_keys = set(list(d1.keys()) + list(d2.keys()))
    diff_dict = defaultdict(tuple)
    for key in all_keys:
        diff_dict[key] = build_diff_for_key(d1, d2, key)
    return diff_dict
