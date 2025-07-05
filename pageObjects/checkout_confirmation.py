from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:
    def __init__(self,driver):
        self.driver= driver
        self.actions = ActionChains(self.driver)
        self.checkout_button = (By.XPATH, "//button[contains(text(), 'Checkout')]")
        self.suggestions = (By.XPATH, "//div[@class='suggestions']//a")
        self.submit = (By.XPATH, "//input[@type='submit']")
        self.alert =(By.CLASS_NAME, "alert")

    def checkout(self):
        checkoutButton = self.driver.find_element(*self.checkout_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkoutButton)
        self.actions.move_to_element(checkoutButton).click().perform()

    def enter_delivery_address(self,countryName):
        self.driver.find_element(By.ID, "country").send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.suggestions))

        countries = self.driver.find_elements(*self.suggestions)

        print(len(countries))

        for country in countries:
            if country.text == "India":
                country.click()
                break

        purchase_button = self.driver.find_element(*self.submit)
        purchase_button.click()


    def validate_order(self):
        success_alert = self.driver.find_element(*self.alert)
        print(success_alert.text)
        assert "Success" in success_alert.text

