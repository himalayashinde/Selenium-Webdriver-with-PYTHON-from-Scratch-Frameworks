import pytest


# fixtures are used for setup and teardown methods for test cases
# conftest file to generalize fixtures and make it available to all test cases

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps is fixtureDemo method")


    def test_fixtureDemo1(self):
        print("I will execute steps is fixtureDemo1 method")


    def test_fixtureDemo2(self):
        print("I will execute steps is fixtureDemo2 method")


    def test_fixtureDemo3(self):
        print("I will execute steps is fixtureDemo3 method")


