from selenium.webdriver.common.by import By

from ui.pages.basePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'title': ('By.CSS_SELECTOR', "h1.title"),
    }

    def get_title(self) -> str:
        return self.title.text

