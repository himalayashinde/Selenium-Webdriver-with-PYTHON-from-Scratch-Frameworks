# any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in methods
# Method names should have sense
# -k starts for method names execution ,
# -s logs in o/p
# -v stands for more information about metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run  with -m
# you can skip tests with @pytest.mark.skip
from traceback import print_tb

import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg="Hello"
    assert msg =="Hi", "Test failed because string do not match"


def test_SecondGreetCreditCard(setup):
    a=4
    b=6
    assert a+2 == 6, "Addition do not match"

