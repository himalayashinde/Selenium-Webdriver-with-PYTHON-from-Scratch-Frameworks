import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

base_dir = os.path.dirname(__file__)
print(base_dir)

# Construct path to the ChromeDriver inside the resources folder
driver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")

service_obj = Service(driver_path)
driver= webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
# driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

print(driver.title)

driver.find_element(By.LINK_TEXT,"Click Here").click()

windowsOpened = driver.window_handles

print(windowsOpened)

driver.switch_to.window(windowsOpened[1])

msg = driver.find_element(By.TAG_NAME,"h3").text

print(msg)

driver.close()

driver.switch_to.window(windowsOpened[0])

msg1 = driver.find_element(By.TAG_NAME,"h3").text

print(msg1)