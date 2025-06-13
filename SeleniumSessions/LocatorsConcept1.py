import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://classic.crmpro.com/")
print(driver.title)

username= driver.find_element(By.NAME, "username" )
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.XPATH, "//input[@value='Login']")





username.send_keys("a30101996j")
password.send_keys("Test@123")
login.click()


input("Press Enter to exit...")