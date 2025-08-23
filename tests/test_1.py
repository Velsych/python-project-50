import difference_calculator
import pytest


@pytest.fixture
def json_correct_flat():
    with open("tests/test_data/flat_data.txt","r") as f:
        json = f.read()
    return json

@pytest.fixture
def json_correct_not_flat():
    with open("tests/test_data/not_flat_data.txt","r") as f:
        json_not_flat = f.read()
    return json_not_flat


@pytest.fixture
def file1_flat():
    return "tests/file1.json"

@pytest.fixture
def file2_flat():
    return "tests/file2.json"

@pytest.fixture
def file1_not_flat():
    return "tests/not_flat.json"

@pytest.fixture
def file2_not_flat():
    return "tests/not_flat2.json"






def test_json_flat(file1_flat,file2_flat,json_correct_flat):
    formatted = difference_calculator.parse_module.generate_diff(file1_flat,file2_flat)
    assert formatted == json_correct_flat



def test_json_not_flat(file1_not_flat,file2_not_flat,json_correct_not_flat):
    formatted = difference_calculator.parse_module.generate_diff(file1_not_flat,file2_not_flat)
    assert formatted == json_correct_not_flat