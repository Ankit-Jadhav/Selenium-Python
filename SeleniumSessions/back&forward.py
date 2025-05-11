import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")
time.sleep(5)

driver.find_element(By.XPATH, '//span[text() = "Mobiles"]').click()

time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.back()

#for refresh
driver.refresh()

input("Enter")

