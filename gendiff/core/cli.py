import argparse


def create_parser():  # pragma: no cover  NOSONAR
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("-f", "--format",
                         help="set format of output", default="stylish")
    parser.add_argument("first_file", default=argparse.SUPPRESS)
    parser.add_argument("second_file", default=argparse.SUPPRESS)
    return parser
    

