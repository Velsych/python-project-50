import argparse

from difference_calculator.core.modules import parse_module


def doc_start():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("-f", "--format", help="set format to output")
    parser.add_argument("first_file", default=argparse.SUPPRESS)
    parser.add_argument("second_file", default=argparse.SUPPRESS)
    args = parser.parse_args()
    file1 = parse_module.file_parser(args.first_file)
    file2 = parse_module.file_parser(args.second_file)
    difference = parse_module.generate_diff(file1, file2)
    return difference, args.format

