from gendiff import generate_diff
import pytest


def test_generate_diff_stylish():
    """test two not empty files with stylish format"""
    with open('tests/fixtures/result1.txt', 'r') as file:
        f = file.read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == f


def test_generate_diff_plain():
    """test two not empty files with plain format"""
    with open('tests/fixtures/result2.txt', 'r') as file:
        f = file.read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain') == f


def test_generate_diff_json():
    """test two not empty files with plain format"""
    with open('tests/fixtures/result3.txt', 'r') as file:
        f = file.read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json') == f


def test_generate_diff_wrong_format():
    """test two not empty files"""
    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.wrong')
