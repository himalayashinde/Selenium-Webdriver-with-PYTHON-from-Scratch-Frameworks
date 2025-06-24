import time

from selenium import webdriver

print("\nChrome Browser Values below\n")

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)


print("\nEdge Browser Values below\n")
driver1= webdriver.Edge()
driver1.get("https://www.google.com/")
print(driver1.title)
print(driver1.current_url)


print("\nFireFox Browser Values below\n")
driver1= webdriver.Firefox()
driver1.get("https://www.google.com/")
print(driver1.title)
print(driver1.current_url)
time.sleep(5)
