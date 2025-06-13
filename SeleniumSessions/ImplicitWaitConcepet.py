import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#  maximum time = 10 sec
#dynamic nature
#Implicit wait will be applied for all the web elements on page
#global wait
#can be applied on find_element and find_elements
#only for web elements --- whatever you see on the page applicable to that only. not for hidden links, title or alert.etc
#not for non web elements = title, url, alerts, etc



driver.get("https://classic.crmpro.com/")
print(driver.title)   #for title we have to give explicit wait because it is not cover under implicit wait
driver.implicitly_wait(2)   #overwrite the previous implicit wait

username= driver.find_element(By.NAME, "username" )
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.XPATH, "//input[@value='Login']")

driver.implicitly_wait(0)    #nullify the implicit wait
username.send_keys("a30101996j")
password.send_keys("Test@123")
login.click()


