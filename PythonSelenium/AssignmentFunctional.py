import os
import time

from selenium import webdriver
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

driver.implicitly_wait(2)
# driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise")

expectedList=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualList=[]

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

time.sleep(2)

results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0

for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()

print(actualList)
assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH," //button[text()='PROCEED TO CHECKOUT']").click()

# time.sleep(2)
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum =0

for price in prices:
    sum = sum + int(price.text)

print(sum)

totalAmount= int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

# time.sleep(5)
# promoInfoElement = By.CLASS_NAME,"promoInfo"

wait = WebDriverWait(driver,10)

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))

promoInfo = driver.find_element(By.CLASS_NAME,"promoInfo").text
print(promoInfo)

assert promoInfo == "Code applied ..!"

discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert totalAmount > discountedAmount