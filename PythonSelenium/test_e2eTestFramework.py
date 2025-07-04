import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage


def test_e2e(browserInstance):
    driver = browserInstance

    driver.maximize_window()

    actions = ActionChains(driver)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    loginPage = LoginPage()

    loginPage.login()

    driver.find_element(By.LINK_TEXT, "Shop").click()

    # //button[text()="Add "]/parent::div/parent::div/parent::app-card//h4/a[text()='Blackberry']
    add_button = (By.XPATH, "//h4/a[text()='Blackberry']/ancestor::app-card//button[text()='Add ']")
    element = driver.find_element(*add_button)
    # Ensure it's in viewport for Firefox
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    actions.move_to_element(driver.find_element(*add_button)).perform()

    driver.find_element(*add_button).click()

    checkout = driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout")
    # element1=driver.find_element(*checkout)
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout)
    actions.move_to_element(checkout).click().perform()
    # checkout.click()

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