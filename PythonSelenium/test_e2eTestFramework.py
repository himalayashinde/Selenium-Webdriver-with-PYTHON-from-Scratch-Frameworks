import os.path
import sys
import time
from selenium import webdriver
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage
from pageObjects.checkout_confirmation import Checkout_Confirmation

def test_e2e(browserInstance):
    driver = browserInstance

    driver.maximize_window()
    # actions= ActionChains(driver)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    loginPage = LoginPage(driver)

    shop_page=loginPage.login()
    shop_page.add_product_to_cart("Blackberry")

    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ind")
    checkout_confirmation.validate_order()
    # need to learn more on it