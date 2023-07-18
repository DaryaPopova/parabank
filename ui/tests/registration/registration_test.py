import json
import logging
import os
import time
import pytest

from ui.entities.user import User
from ui.pages.registration_page import RegistrationPage

logger = logging.getLogger()


def get_data() -> list[User]:
    json_path = os.path.join(os.path.dirname(__file__), "registration_test_data.json")
    with open(json_path) as json_file:
        data = json.load(json_file)
    return data


@pytest.mark.parametrize("user_data", get_data())
def test_registration_form(driver, user_data):

    user_data["username"] += str(time.time_ns() % 1000000)
    user = User(**user_data)

    registration_page: RegistrationPage = RegistrationPage(driver)
    logger.info("Filling registration form")
    registration_page.fill_form(user)

    home_page = registration_page.submit_form(driver)
    actual_title = home_page.get_title()
    expected_title = "Welcome {username}".format(username=user.username)
    assert actual_title == expected_title
