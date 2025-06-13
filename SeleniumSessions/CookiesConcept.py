import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.reddit.com/")
time.sleep(5)

#method 1
print(driver.get_cookies())
print(len(driver.get_cookies()))   #how many cookies are there
# add new cookie
driver.add_cookie({"name":"Python", "value":"Python", "domain": "reddit.com"})

# method 2
cookies = driver.get_cookies()

for i in cookies:
    print(i)
