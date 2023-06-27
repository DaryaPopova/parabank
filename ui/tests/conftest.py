import logging
import sys
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui.pages.registrationPage import RegistrationPage

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@pytest.fixture()
def driver():
    logger.info("Running class setUp")

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    driver.implicitly_wait(5)
    driver.maximize_window()
    assert RegistrationPage(driver).get_title() == 'Signing up is easy!'

    yield driver

    logger.info("Running class tearDown")
    driver.quit()
