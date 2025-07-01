import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browserSortedVeggies=[]

base_dir = os.path.dirname(__file__)
print(base_dir)

# Construct path to the ChromeDriver inside the resources folder
driver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")

service_obj = Service(driver_path)
driver= webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
# driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# collect all veggie names -> veggieList //tr/td[1]
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# sort this veggieList => newSortedList
browserSortedVeggies.sort()

# veggieList == newSortedList
assert browserSortedVeggies == originalBrowserSortedList

