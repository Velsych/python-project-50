#!  /.venv/bin/python
from difference_calculator import doc_gendiff
from difference_calculator.core.modules import parse_module


def main():  # NOSONAR
    parser = doc_gendiff.doc_start()
    args = parser.parse_args()
    diff = parse_module.generate_diff(args.first_file,
                                       args.second_file, args.format)
    print(diff)


if __name__ == "__main__":  # NOSONAR
    main()