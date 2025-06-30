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

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

print(driver.title)

driver.find_element(By.XPATH,"(//a)[1]").click()

windowsOpened = driver.window_handles

print(windowsOpened)

driver.switch_to.window(windowsOpened[1])

print(driver.title)

email = driver.find_element(By.XPATH,"//p[@class='im-para red']/strong").text

print(email)

driver.close()

driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID,"username").send_keys(email)

# password

driver.find_element(By.ID,"password").send_keys(email)

# terms

driver.find_element(By.ID,"terms").click()

# signInBtn
driver.find_element(By.ID,"signInBtn").click()

# time.sleep(5)

wait = WebDriverWait(driver,10)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']")))

warningMsg = driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text

print(warningMsg)

assert "Incorrect" in warningMsg
