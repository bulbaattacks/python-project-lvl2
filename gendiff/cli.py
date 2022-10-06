import argparse


def argument_parser():
    parser = argparse.ArgumentParser(description='''Compares two configuration
    files and shows a difference.''')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')
    parser.add_argument('-V', '--version', help='set format of output')
    return parser.parse_args()
