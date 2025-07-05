from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import Checkout_Confirmation


class ShopPage:

    def __init__(self,driver):
        self.driver = driver
        self.shop_link= (By.LINK_TEXT, "Shop")
        self.actions = ActionChains(self.driver)
        self.checkout_button = (By.PARTIAL_LINK_TEXT, "Checkout")

    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()

        # //button[text()="Add "]/parent::div/parent::div/parent::app-card//h4/a[text()='Blackberry']
        add_button = (By.XPATH, "//h4/a[text()='"+product_name+"']/ancestor::app-card//button[text()='Add ']")
        element = self.driver.find_element(*add_button)
        # Ensure it's in viewport for Firefox
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # actions = ActionChains(self.driver)
        self.actions.move_to_element(self.driver.find_element(*add_button)).perform()

        self.driver.find_element(*add_button).click()


    def goToCart(self):
        checkout = self.driver.find_element(*self.checkout_button)
        # element1=driver.find_element(*checkout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout)
        self.actions.move_to_element(checkout).click().perform()
        # checkout.click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation

