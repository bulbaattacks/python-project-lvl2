from gendiff.parser import parser_content
from gendiff.dicts_builder import diff_builder
from gendiff.formatters.stylish import format_stylish


def get_content(path):
    with open(path, 'r') as file_content:
        return parser_content(file_content.read(), path.split('.')[-1])


def generate_diff(file1, file2):
    source1 = get_content(file1)
    source2 = get_content(file2)

    diff = diff_builder(source1, source2)

    return format_stylish(diff)
