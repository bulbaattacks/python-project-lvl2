import json


def json_maker(diff_dict):
    return json.dumps(diff_dict, sort_keys=True, indent=1)


def format_json(diff_dict):
    return json_maker(diff_dict)
