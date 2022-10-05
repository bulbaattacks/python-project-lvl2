from gendiff import generate_diff
import pytest


@pytest.mark.parametrize("format,expected",
                         [("stylish", "tests/fixtures/result1.txt"),
                          ("plain", "tests/fixtures/result2.txt"),
                          ("json", "tests/fixtures/result3.txt")])
def test_generate_diff(format, expected):
    """test two not empty files"""
    with open(expected, 'r') as file:
        f = file.read()
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', format) == f


def test_generate_diff_wrong_format():
    """test two not empty files with wrong_format of a file"""
    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.wrong')
