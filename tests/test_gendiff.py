from gendiff import generate_diff
import pytest
import os


def generate_fixture_path(file_name):
    return os.path.join("tests", "fixtures", file_name)


@pytest.mark.parametrize("file1, file2, format, expected",
                         [("file1.json", "file2.json", "stylish", "result1.txt"),
                          ("file1.json", "file2.json", "plain", "result2.txt"),
                          ("file1.json", "file2.json", "json", "result3.txt")])
def test_generate_diff(file1, file2, format, expected):
    """test two not empty files"""
    full_file_name = generate_fixture_path(expected)
    path_to_file1 = generate_fixture_path(file1)
    path_to_file2 = generate_fixture_path(file2)
    with open(full_file_name, 'r') as file:
        result = file.read()
        assert generate_diff(path_to_file1, path_to_file2, format) == result


@pytest.mark.parametrize("right_format_file, wrong_format_file",
                         [("file1.json", "file2.wrong")])
def test_generate_diff_wrong_format(right_format_file, wrong_format_file):
    """test two not empty files with wrong_format of a file"""
    path_to_right_format_file = generate_fixture_path(right_format_file)
    path_to_wrong_format_file = generate_fixture_path(wrong_format_file)
    with pytest.raises(Exception):
        generate_diff(path_to_right_format_file, path_to_wrong_format_file)
