from gendiff.parser import parser_content
from gendiff.dicts_builder import diff_builder
from gendiff.formatters import formatter


def get_content(path):
    with open(path, 'r') as file_content:
        return parser_content(file_content.read(), path.split('.')[-1])


def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    content1 = get_content(path_to_file1)
    content2 = get_content(path_to_file2)

    diff = diff_builder(content1, content2)

    return formatter(format, diff)
