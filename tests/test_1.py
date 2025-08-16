import difference_calculator



def test_json():
    file_1 = "tests/file1.json"
    file_2 = "tests/file2.json"
    assert difference_calculator.parse_module.generate_diff(file_1,file_2) == """{ 
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + host: hexlet.io
    + verbose: true
}"""

def test_yaml():
    file1 = "tests/file1.yml"
    file2 = "tests/file2.yaml"
    assert difference_calculator.parse_module.generate_diff(file1,file2) ==  """{ 
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + host: hexlet.io
    + verbose: true
}"""

def test_json_and_yaml():
    file1 = "tests/file1.json"
    file2 = "tests/file2.yaml"
    assert difference_calculator.parse_module.generate_diff(file1,file2) ==  """{ 
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + host: hexlet.io
    + verbose: true
}"""
#