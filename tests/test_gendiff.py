from gendiff import generate_diff
import pytest
import os


def fixture_path_constructor(file_name):
    return os.path.join("tests", "fixtures", file_name)


@pytest.mark.parametrize("format,expected",
                         [("stylish", "result1.txt"),
                          ("plain", "result2.txt"),
                          ("json", "result3.txt")])
def test_generate_diff(format, expected):
    """test two not empty files"""
    full_file_name = fixture_path_constructor(expected)
    with open(full_file_name, 'r') as file:
        f = file.read()
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', format) == f


def test_generate_diff_wrong_format():
    """test two not empty files with wrong_format of a file"""
    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.wrong')
