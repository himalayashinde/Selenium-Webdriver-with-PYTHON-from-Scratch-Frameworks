import json
import os.path
import sys
import time

import pytest
from selenium import webdriver
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage
from pageObjects.checkout_confirmation import Checkout_Confirmation
test_data_path="../data/test_e2eTestFramework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list= test_data["data"]


@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance

    driver.maximize_window()
    # actions= ActionChains(driver)

    loginPage = LoginPage(driver)

    shop_page=loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])

    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ind")
    checkout_confirmation.validate_order()
    # need to learn more on it