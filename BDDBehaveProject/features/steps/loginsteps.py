from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    

@when('I open OrangeHRM Homepage')
def (context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   
@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user , pwd):
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//button[text() = " Login "]' ).click()
   
@then('User must successfully login to the Dashboard page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//h6[contains(text(), "Dashboard")]').click()
    

   