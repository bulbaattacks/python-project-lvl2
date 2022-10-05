import argparse


def informator():
    parser = argparse.ArgumentParser(description='''Compares two configuration
    files and shows a difference.''')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')
    parser.add_argument('-V', '--version', help='set format of output')
    args = parser.parse_args()
    return args