import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed Last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Himalaya","Shinde","rahulshettyacademy.com"]

@pytest.fixture(params=[("Chrome","Rahul","Shetty"),("Firefox","Himalaya"),("IE","WHY NOT MORE")])
def crossBrowser(request):
    return request.param

