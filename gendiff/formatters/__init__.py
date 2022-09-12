from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def formatter(format, diff_dict):
    format_chooser = {
        "plain": format_plain,
        "stylish": format_stylish
    }
    return format_chooser[format](diff_dict)
