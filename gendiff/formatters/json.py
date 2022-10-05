import json


def format_json(diff_dict):
    return json.dumps(diff_dict, sort_keys=True, indent=1)
