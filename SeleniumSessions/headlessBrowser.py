import time
from selenium import webdriver
from selenium.webdriver.common.by import By


option= webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument("--incognito")


driver= webdriver.Chrome(options=option)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")
time.sleep(10)
print(driver.title)

input("Exit")