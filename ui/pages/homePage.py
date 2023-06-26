from selenium.webdriver.common.by import By

from ui.pages.basePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, "h1.title").text

