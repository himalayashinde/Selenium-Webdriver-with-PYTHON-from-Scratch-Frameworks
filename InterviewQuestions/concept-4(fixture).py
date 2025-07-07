import pytest


@pytest.fixture
def sample_testdata():
    print("\n Setup creating test data")
    data= {"name" : "Alice", "age": 30 }
    yield data
    print("Cleaning up test data")

def test_example(sample_testdata):
    assert sample_testdata["name"] == "Alice"
    assert sample_testdata["age"] == 30
    print("Test executed successfully")

