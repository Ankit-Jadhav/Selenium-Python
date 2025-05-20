import time
from logging import makeLogRecord

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://app.hubspot.com/login")
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "#username").send_keys("a30101996j")   #input email
driver.find_element(By.CLASS_NAME, "private-button--primary").click()       #click on next

#click on logo
driver.find_element(By.CLASS_NAME, "Image__StyledImage-sc-966akd-0.glezya").click()    #note : for spaces we can use " . "in the class , we can also use "tag."
#Image__StyledImage-sc-966akd-0.glezya
#img.Image__StyledImage-sc-966akd-0.glezya
time.sleep(5)


#creating xpath with class
#click on hamburger
driver.find_element(By.XPATH, "//span[@class='global-nav-tab-title cl-navLink-link ga_nav_link']").click( )






# uiButton private-button private-button--primary private-button--default private-button--block private-button--non-link
# uiButton private-button private-button--tertiary private-button--default private-button--block disabled private-button--disabled private-button--non-link
input("Please enter to exit")


#Notes:
'''
# 1. ID
element = driver.find_element(By.ID, "loginBtn")
2. Name
element = driver.find_element(By.NAME,  "username")
3. Class Name
# Use only one class (cannot handle multiple class names directly).
element = driver.find_element(By.NAME, "login-input")
4. Locates by HTML tag like input, a, div, etc.
elements = driver.find_element(By.TAG_NAME, "h1")
5. Link Text
#Locates entire visible text of a link.
element = driver.find_element(By.LINK_TEXT, "Login")
6. Partial link text
#locates link by partial visible text.
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
7.XPATH
Best for flexible targeting. Basic XPath with attribute:
element = driver.find_element(By.XPATH, "//input[@id='username']")
XPath with contains()(useful for class with spaces):
element = driver.find_element(By.XPATH, "//span[contains@class, 'navLink-link']")   many more\
8. CSS selectors
Often more readable than xpath and faster

#ID
element = driver.find_element(By.CSS_SELECTOR, "#login-input")

#Class
element = driver.find_element(By.CSS_SELECTOR, ".login-input")

# Class with multiple classes:
element = driver.find_element(By.CSS_SELECTOR, ".btn.primary.large")

#Attribute match
element = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

#Partial attribute match
element = driver.find_element(By.CSS_SELECTOR, "input[name* = 'user']")

'''



