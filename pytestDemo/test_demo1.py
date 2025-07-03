# any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in methods
# @pytest.mark.xfail to complete the execution without reporting
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest

@pytest.mark.xfail
def test_firstProgram(setup):
    print("hello i am pytest")

@pytest.mark.smoke
def test_SecondCreditCard():
    print("GoodMorning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])