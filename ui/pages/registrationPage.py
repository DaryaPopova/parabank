from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.entities import User
from ui.pages.homePage import HomePage
from ui.pages.basePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'first_name': ('ID', "customer.firstName"),
        'last_name': ('ID', "customer.lastName"),
        'address_street': ('ID', "customer.address.street"),
        'address_city': ('ID', "customer.address.city"),
        'address_state': ('ID', "customer.address.state"),
        'address_zip_code': ('ID', "customer.address.zipCode"),
        'phone_number': ('ID', "customer.phoneNumber"),
        'ssn': ('ID', "customer.ssn"),
        'username': ('ID', "customer.username"),
        'password': ('ID', "customer.password"),
        'repeated_password': ('ID', "repeatedPassword"),
    }

    def fill_form(self, user: User):
        print("Filling registration form")
        self.first_name.send_keys(user.first_name)
        self.last_name.send_keys(user.last_name)
        self.address_street.send_keys(user.address_street)
        self.address_city.send_keys(user.address_city)
        self.address_state.send_keys(user.address_state)
        self.address_zip_code.send_keys(user.address_zip_code)
        self.phone_number.send_keys(user.phone_number)
        self.ssn.send_keys(user.ssn)
        self.username.send_keys(user.username)
        self.password.send_keys(user.password)
        self.repeated_password.send_keys(user.repeated_password)

    def submit_form(self, driver) -> HomePage:
        print("Submitting registration form")
        self.driver.find_element(By.CSS_SELECTOR, "form#customerForm input.button").click()
        return HomePage(driver)

    def wait_for_welcome_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome')]")))

    def get_title(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, "h1.title").text

    def get_different_passwords_message(self) -> str:
        return self.driver.find_element(By.ID, "repeatedPassword.errors").text
