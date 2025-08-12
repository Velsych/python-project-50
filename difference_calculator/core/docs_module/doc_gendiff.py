import argparse

from difference_calculator.core.modules import parse_module


def doc_start(): # pragma: no cover
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("-f", "--format", help="set format to output")
    parser.add_argument("first_file", default=argparse.SUPPRESS)
    parser.add_argument("second_file", default=argparse.SUPPRESS)
    return parser
    

