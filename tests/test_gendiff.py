from gendiff import generate_diff
import pytest
import os


def generate_fixture_path(file_name):
    return os.path.join("tests", "fixtures", file_name)


@pytest.mark.parametrize("format,expected",
                         [("stylish", "result1.txt"),
                          ("plain", "result2.txt"),
                          ("json", "result3.txt")])
def test_generate_diff(format, expected):
    """test two not empty files"""
    full_file_name = generate_fixture_path(expected)
    with open(full_file_name, 'r') as file:
        result = file.read()
        path_to_file1 = generate_fixture_path('file1.json')
        path_to_file2 = generate_fixture_path('file2.json')
        assert generate_diff(path_to_file1, path_to_file2, format) == result


def test_generate_diff_wrong_format():
    """test two not empty files with wrong_format of a file"""
    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.wrong')
