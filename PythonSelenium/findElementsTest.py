import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Get the current directory (where demoBrowser.py is)
base_dir = os.path.dirname(__file__)
print(base_dir)

# Construct path to the ChromeDriver inside the resources folder
driver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")

service_obj = Service(driver_path)
driver= webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)

# //li[@class='ui-menu-item']/a[text()='India']

countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID,"autosuggest").text)
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

validate_Country=  driver.find_element(By.ID,"autosuggest").get_attribute("value")

assert validate_Country == "India"

time.sleep(5)