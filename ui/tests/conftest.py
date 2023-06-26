import os
import json

import pytest

from selenium import webdriver

from ui.pages.registrationPage import RegistrationPage


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
