import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.entities import user
from ui.pages.home_page import HomePage
from ui.pages.base_page import BasePage

logger = logging.getLogger()


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
        'submit_button': ('CSS', "form#customerForm input.button"),
        'welcome_title': ('XPATH', "//h1[contains(text(), 'Welcome')]"),
        'title': ('CSS', "h1.title"),
        'repeated_password_errors_message': ('ID', "repeatedPassword.errors")
    }

    def fill_form(self, user: User):
        logger.info("Fill first name")
        self.first_name.send_keys(user.first_name)
        logger.info("Fill last name")
        self.last_name.send_keys(user.last_name)
        logger.info("Fill address street")
        self.address_street.send_keys(user.address_street)
        logger.info("Fill address city")
        self.address_city.send_keys(user.address_city)
        logger.info("Fill address state")
        self.address_state.send_keys(user.address_state)
        logger.info("Fill address zip code")
        self.address_zip_code.send_keys(user.address_zip_code)
        logger.info("Fill address phone number")
        self.phone_number.send_keys(user.phone_number)
        logger.info("Fill SSN")
        self.ssn.send_keys(user.ssn)
        logger.info("Fill username")
        self.username.send_keys(user.username)
        logger.info("Fill password")
        self.password.send_keys(user.password)
        logger.info("Fill confirmation of password")
        self.repeated_password.send_keys(user.repeated_password)

    def submit_form(self, driver) -> HomePage:
        logger.info("Submitting registration form")
        self.submit_button.click()
        return HomePage(driver)

    def wait_for_welcome_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.welcome_title))

    def get_title(self) -> str:
        return self.title.text

    def get_different_passwords_message(self) -> str:
        return self.repeated_password_errors_message.text
