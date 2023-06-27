from typing import Type

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.entities import User
from ui.pages.homePage import HomePage
from ui.pages.basePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, user: User):
        print("Filling registration form")
        self.driver.find_element(By.ID, "customer.firstName").send_keys(user.first_name)
        self.driver.find_element(By.ID, "customer.lastName").send_keys(user.last_name)
        self.driver.find_element(By.ID, "customer.address.street").send_keys(user.address_street)
        self.driver.find_element(By.ID, "customer.address.city").send_keys(user.address_city)
        self.driver.find_element(By.ID, "customer.address.state").send_keys(user.address_state)
        self.driver.find_element(By.ID, "customer.address.zipCode").send_keys(user.address_zip_code)
        self.driver.find_element(By.ID, "customer.phoneNumber").send_keys(user.phone_number)
        self.driver.find_element(By.ID, "customer.ssn").send_keys(user.ssn)
        self.driver.find_element(By.ID, "customer.username").send_keys(user.username)
        self.driver.find_element(By.ID, "customer.password").send_keys(user.password)
        self.driver.find_element(By.ID, "repeatedPassword").send_keys(user.repeated_password)

    def submit_form(self, driver) -> HomePage:
        print("Submitting registration form")
        self.driver.find_element(By.CSS_SELECTOR, "form#customerForm input.button").click()
        return HomePage(driver)

    def get_title(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, "h1.title").text

    def get_different_passwords_message(self) -> str:
        return self.driver.find_element(By.ID, "repeatedPassword.errors").text

