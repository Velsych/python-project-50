import difference_calculator
import pytest


def test1():
    file_1 = difference_calculator.parse_module.file_parser("tests/file1.json")
    file_2 = difference_calculator.parse_module.file_parser("tests/file2.json")
    assert difference_calculator.parse_module.generate_diff(file_1,file_2) == """{ 
    - follow: False
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + host: hexlet.io
    + verbose: True
}"""



