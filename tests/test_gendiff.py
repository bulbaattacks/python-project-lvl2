from gendiff import generate_diff


def test_generate_diff():
    with open('/tests/fixtures/result_fil1_file2.txt', 'r') as file:
        f = file.read()
    assert generate_diff('/Users/arinazubova/super_hexlet/python-project-lvl2/tests/fixtures/file1.json', '/Users/arinazubova/super_hexlet/python-project-lvl2/tests/fixtures/file2.json') == f
