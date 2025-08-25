import difference_calculator
import pytest


@pytest.fixture
def stylish_correct_flat():
    with open("tests/test_data/flat_data.txt","r") as f:
        stylish = f.read()
    return stylish

@pytest.fixture
def stylish_correct_not_flat():
    with open("tests/test_data/not_flat_data.txt","r") as f:
        stylish_not_flat = f.read()
    return stylish_not_flat

@pytest.fixture
def plain_correct_flat():
    with open("tests/test_data/plain_flat.txt","r") as f:
        plain = f.read()
    return plain

@pytest.fixture
def plain_correct():
    with open("tests/test_data/plain_not_flat.txt","r") as f:
        plain_flat = f.read()
    return plain_flat


@pytest.fixture
def json_flat_correct():
    with open("tests/test_data/true_json_flat.json","r") as f:
        json_flat = f.read()
    return json_flat

@pytest.fixture
def json_not_flat_correct():
    with open("tests/test_data/true_json.json","r") as f:
        json = f.read()
    return json



@pytest.fixture
def file1_flat():
    return "tests/file1.json"

@pytest.fixture
def file2_flat():
    return "tests/file2.yaml"

@pytest.fixture
def file1_not_flat():
    return "tests/not_flat.json"

@pytest.fixture
def file2_not_flat():
    return "tests/not_flat2.json"






def test_stylish_flat(file1_flat,file2_flat,stylish_correct_flat):
    formatted = difference_calculator.parse_module.generate_diff(file1_flat,file2_flat,"stylish")
    assert formatted == stylish_correct_flat



def test_stylish_not_flat(file1_not_flat,file2_not_flat,stylish_correct_not_flat):
    formatted = difference_calculator.parse_module.generate_diff(file1_not_flat,file2_not_flat,"stylish")
    assert formatted == stylish_correct_not_flat


def test_plain_not_flat(file1_not_flat,file2_not_flat,plain_correct):
    formatted = difference_calculator.parse_module.generate_diff(file1_not_flat,file2_not_flat,"plain")
    assert formatted == plain_correct


def test_plain_flat(file1_flat,file2_flat,plain_correct_flat):
    formatted = difference_calculator.parse_module.generate_diff(file1_flat,file2_flat,"plain")
    assert formatted == plain_correct_flat


def test_json_flat(file1_flat,file2_flat,json_flat_correct):
    formatted = difference_calculator.parse_module.generate_diff(file1_flat,file2_flat,"json")
    assert formatted == json_flat_correct

def test_json_not_flat(file1_not_flat,file2_not_flat,json_not_flat_correct):
    formatted = difference_calculator.parse_module.generate_diff(file1_not_flat,file2_not_flat,"json")
    assert formatted == json_not_flat_correct