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

driver.get("https://the-internet.herokuapp.com/iframe")

driver.find_element(By.XPATH,"//div[@class='tox-icon']").click()

driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID,"tinymce").clear()

driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")



