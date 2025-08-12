import difference_calculator



def test1():
    file_1 = "tests/file1.json"
    file_2 = "tests/file2.json"
    assert difference_calculator.parse_module.generate_diff(file_1,file_2) == """{ 
    - follow: False
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + host: hexlet.io
    + verbose: True
}"""
