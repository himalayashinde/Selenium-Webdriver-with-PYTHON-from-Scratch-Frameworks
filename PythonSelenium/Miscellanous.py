import os.path
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

base_dir= os.path.dirname(__file__)
print(base_dir)
driver_paths= os.path.join(base_dir,"chromedriver-win64","chromedriver.exe")
print(driver_paths)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj1= Service(driver_paths)
driver= webdriver.Chrome(service=service_obj1,options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(5)
# scroll to the specified screen location

driver.execute_script("window.scroll(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("screen.png")
