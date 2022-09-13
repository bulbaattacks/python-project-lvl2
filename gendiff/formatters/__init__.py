from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def formatter(format, diff_dict):
    format_chooser = {
        "plain": format_plain,
        "stylish": format_stylish,
        "json": format_json
    }
    return format_chooser[format](diff_dict)
