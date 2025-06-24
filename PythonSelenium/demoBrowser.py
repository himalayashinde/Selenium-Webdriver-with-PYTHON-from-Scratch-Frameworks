import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Get the current directory (where demoBrowser.py is)
base_dir = os.path.dirname(__file__)
print(base_dir)

# Construct path to the ChromeDriver inside the resources folder
driver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")

service_obj = Service(driver_path)
driver= webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/locatorspractice/")

time.sleep(5)