from collections import defaultdict


def build_for_diff_dicts(dict1, dict2, key):
    if key not in dict1:
        return {
            'action': 'record added',
            'value': dict2.get(key)
        }
    if key not in dict2:
        return {
            'action': 'record deleted',
            'value': dict1.get(key)
        }
    if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
        return {
            'action': 'record nested',
            'children': diff_builder(dict1[key], dict2[key])
        }
    if dict1.get(key) != dict2.get(key):
        return {
            'action': 'record changed',
            'previous': dict1.get(key),
            'current': dict2.get(key)
        }

    return {
        'action': 'record is the same',
        'value': dict1.get(key)
        }


def diff_builder(dict1, dict2):
    all_keys = set(list(dict1.keys()) + list(dict2.keys()))
    diff_dict = defaultdict(tuple)
    for key in all_keys:
        diff_dict[key] = build_for_diff_dicts(dict1, dict2, key)
    return diff_dict
