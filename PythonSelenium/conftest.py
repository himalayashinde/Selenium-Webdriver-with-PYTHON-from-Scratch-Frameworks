from email.policy import default

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome",help="ByDefault Chrome selected as commandline argument not provided"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name= request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()

        # Disable Chrome's password manager and autofill features
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "profile.default_content_setting_values.popups": 0,
            "autofill.profile_enabled": False,
            "autofill.enabled": False,
        }

        options.add_experimental_option("prefs", prefs)

        # Open Chrome in incognito mode to avoid saved sessions
        options.add_argument("--incognito")

        driver = webdriver.Chrome(options=options)
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