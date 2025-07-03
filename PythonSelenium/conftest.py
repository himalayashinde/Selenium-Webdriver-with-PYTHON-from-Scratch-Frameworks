from email.policy import default

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome",help="ByDefault Chrome selected as commandline argument not provided"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name= request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        yield driver
    elif browser_name == "edge":
        driver = webdriver.Edge()
        driver.implicitly_wait(5)
        yield driver
    else:
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        yield driver    # Before Test function execution
        driver.close()  # Post your function execution