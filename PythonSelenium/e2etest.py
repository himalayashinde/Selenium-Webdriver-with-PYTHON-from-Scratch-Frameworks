import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.maximize_window()

actions = ActionChains(driver)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.LINK_TEXT,"Shop").click()


# //button[text()="Add "]/parent::div/parent::div/parent::app-card//h4/a[text()='Blackberry']
add_button = (By.XPATH,"//h4/a[text()='Blackberry']/ancestor::app-card//button[text()='Add ']")
actions.move_to_element(driver.find_element(*add_button)).perform()

driver.find_element(*add_button).click()

checkout = driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout")

actions.move_to_element(checkout).perform()

checkout.click()

checkoutButton =driver.find_element(By.XPATH,"//button[contains(text(), 'Checkout')]")
actions.move_to_element(checkoutButton).perform()
checkoutButton.click()

driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']//a")))

countries = driver.find_elements(By.XPATH,"//div[@class='suggestions']//a")

print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break


purchase_button = driver.find_element(By.XPATH,"//input[@type='submit']")

purchase_button.click()

success_alert = driver.find_element(By.CLASS_NAME,"alert")
print(success_alert.text)

assert "Success" in success_alert.text

# //div[@class='suggestions']//a[text()='India']
driver.close()

time.sleep(5)
