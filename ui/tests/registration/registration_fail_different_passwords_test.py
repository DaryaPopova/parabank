import json
import logging
import os
import time

from ui.entities.user import User
from ui.pages.registration_page import RegistrationPage

logger = logging.getLogger()


def test_registration_form_different_passwords(driver):
    json_path = os.path.join(os.path.dirname(__file__), "registration_fail_different_passwords_test_data.json")
    with open(json_path) as json_file:
        data = json.load(json_file)

    data["user"]["username"] += str(time.time_ns() % 1000000)
    user = User(**data["user"])

    registration_page: RegistrationPage = RegistrationPage(driver)
    logger.info("Filling registration form with different passwords")
    registration_page.fill_form(user)

    home_page = registration_page.submit_form(driver)
    actual_title = home_page.get_title()
    expected_title = "Signing up is easy!"
    assert actual_title == expected_title

    actual_different_passwords_message = registration_page.get_different_passwords_message()
    expected_different_passwords_message = "Passwords did not match."
    assert actual_different_passwords_message == expected_different_passwords_message
