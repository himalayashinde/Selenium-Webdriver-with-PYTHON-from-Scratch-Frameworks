# Get the current directory (where demoBrowser.py is)
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

base_dir = os.path.dirname(__file__)
print(base_dir)

# Construct path to the ChromeDriver inside the resources folder
driver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")

service_obj = Service(driver_path)
driver= webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID,"name").send_keys("Himalaya")
name= driver.find_element(By.ID,"name").get_attribute("value")
driver.find_element(By.ID,"alertbtn").click()
print(name)
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

# need to understand in depth for python automation