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


def test_e2e(browserInstance):
    driver = browserInstance

    driver.maximize_window()
    actions= ActionChains(driver)

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    loginPage = LoginPage(driver)

    shop_page=loginPage.login()

    shop_page.add_product_to_cart("Blackberry")

    shop_page.goToCart()

    checkoutButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", checkoutButton)
    actions.move_to_element(checkoutButton).click().perform()
    # checkoutButton.click()

    driver.find_element(By.ID, "country").send_keys("Ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']//a")))

    countries = driver.find_elements(By.XPATH, "//div[@class='suggestions']//a")

    print(len(countries))

    for country in countries:
        if country.text == "India":
            country.click()
            break

    purchase_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    purchase_button.click()

    success_alert = driver.find_element(By.CLASS_NAME, "alert")
    print(success_alert.text)

    assert "Success" in success_alert.text

    # //div[@class='suggestions']//a[text()='India']
    time.sleep(5)