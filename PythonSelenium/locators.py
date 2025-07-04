import os.path
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

base_dir= os.path.dirname(__file__)
print(base_dir)
driver_paths= os.path.join(base_dir,"chromedriver-win64","chromedriver.exe")
print(driver_paths)

service_obj1= Service(driver_paths)
driver= webdriver.Chrome(service=service_obj1)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

# Xpath used below for reference
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Himalaya Shinde")

# Name tag
driver.find_element(By.NAME,"email").send_keys("himalayashinde@gmail.com")

# Id
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Himalaya@1234")
driver.find_element(By.ID,"exampleCheck1").click()

# Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

# Xpath -->  //tagname[@attribute='value']
# Css Selector --> tagname[@attribute='value'], #id, .classname

driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message= driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert "Success" in message

driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("Hello World...!!")


time.sleep(5)