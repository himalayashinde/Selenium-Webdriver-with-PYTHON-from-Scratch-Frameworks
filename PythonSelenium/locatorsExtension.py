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

service_obj1= Service(driver_paths)
driver= webdriver.Chrome(service=service_obj1)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()

driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")

driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Himalaya@1234")

driver.find_element(By.ID,"confirmPassword").send_keys("Himalaya@1234")

driver.find_element(By.XPATH," //button[text()='Save New Password']").click()


time.sleep(5)