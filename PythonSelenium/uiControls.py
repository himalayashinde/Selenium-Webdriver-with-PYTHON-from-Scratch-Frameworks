import os.path
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

base_dir=os.path.dirname(__file__)

driver_path3= os.path.join(base_dir,"chromedriver-win64","chromedriver.exe")

service_object= Service(driver_path3)

driver= webdriver.Chrome(service=service_object)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


print("\nCheckBox validation below\n")
checkbox_options = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkbox_options))

for checks in checkbox_options:
    if checks.get_attribute("value") == "option2":
        checks.click()
        assert checks.is_selected()
        break

time.sleep(2)

# radio button validation below
print("\nRadio button validation below\n")
radioButtons = driver.find_elements(By.XPATH,"//input[@type='radio']")

print(len(radioButtons))

for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio2":
        radioButton.click()
        assert radioButton.is_selected()
        break

time.sleep(1)

displayBox = driver.find_element(By.ID,"displayed-text")

assert displayBox.is_displayed()

driver.find_element(By.ID,"hide-textbox").click()

assert not displayBox.is_displayed()

time.sleep(3)
