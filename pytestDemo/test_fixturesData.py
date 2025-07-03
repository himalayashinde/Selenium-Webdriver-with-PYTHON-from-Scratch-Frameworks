import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self,dataLoad):
        print("\n"+dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])
