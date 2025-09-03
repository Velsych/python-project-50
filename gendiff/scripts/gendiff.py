#!  /.venv/bin/python
from gendiff import doc_gendiff
from gendiff.core import diff_generator


def main():  # NOSONAR
    parser = doc_gendiff.create_parser()
    args = parser.parse_args()
    diff = diff_generator.generate_diff(args.first_file,
                                       args.second_file, args.format)
    print(diff)


if __name__ == "__main__":  # NOSONAR
    main()