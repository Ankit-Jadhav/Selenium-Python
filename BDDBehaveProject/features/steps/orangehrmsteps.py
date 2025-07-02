from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
  
@when('open OrangeHRM homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
 
@then('verify that the logo presence on page')
def verifyLogo(context):
    wait = WebDriverWait(context.driver, 10)
    logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='orangehrm-login-branding']/img[@alt='company-branding']")))
    assert logo.is_displayed(), "Logo is not visible on the login page"
    
@then('close browser')
def closeBrowser(context):
    context.driver.quit()
