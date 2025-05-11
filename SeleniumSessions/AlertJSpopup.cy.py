import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
time.sleep(5)

driver.find_element(By.NAME, "proceed").click()
time.sleep(5)

alert = driver.switch_to.alert
alert.accept() #accept it and click on OK
# alert.dismiss() #cancel the popup
#alert.send_keys("Hi")    #this syntax we use when we have popup with input
#driver.switch_to.default_content()
input("Enter to exit")
