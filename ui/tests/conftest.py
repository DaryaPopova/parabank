import logging
import sys
import pytest

from selenium import webdriver

from ui.pages.registrationPage import RegistrationPage

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@pytest.fixture()
def driver():
    print("Running class setUp")

    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    driver.implicitly_wait(5)
    driver.maximize_window()
    assert RegistrationPage(driver).get_title() == 'Signing up is easy!'

    yield driver
    print("Running class tearDown")
    driver.quit()
