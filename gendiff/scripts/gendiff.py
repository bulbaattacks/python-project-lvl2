#!/usr/bin/env python
from gendiff import generate_diff
from gendiff.cli import informator


def main():
    args = informator()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
