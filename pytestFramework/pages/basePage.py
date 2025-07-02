from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
    
    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def type(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def get_title(self):
        return self.driver.title
    
    def is_element_displayed(self,locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator)).is_displayed()
        