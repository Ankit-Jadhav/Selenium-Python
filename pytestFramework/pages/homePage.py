from selenium.webdriver.common.by import By
from pytestFramework.pages.basePage import BasePage


class googleHomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.search_box = (By.NAME, "q")

    def verif_search_box(self):
        return self.is_element_displayed(self.search_box)



