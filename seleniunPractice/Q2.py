import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.reddit.com/")
print(driver.get_cookies())
print(len(driver.get_cookies()))

driver.add_cookie({"name":"Python","value": "Rocks123", "domain": "reddit.com"})

print(driver.get_cookie("Python"))

driver.delete_cookie("Python")
print(driver.get_cookie("Python"))

# Optional: delete all cookies
# driver.delete_all_cookies()


cookies =driver.get_cookies()
for i in cookies:
    print(i)


input("enter to exit")


#In Selenium with Python, cookies are managed using dictionaries. For example, to add a cookie, we use driver.add_cookie() and pass a dictionary with keys like 'name', 'value', 'domain', etc.


