import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")

#innertext
inner_text = driver.execute_script("return document.documentElement.innerText;")
print(inner_text)


mobile_click = driver.find_element(By.XPATH, "//span[text()='Mobiles']")

#highlight the value -- in case of bug ss
print(driver.execute_script("arguments[0].style.border = '3px solid red'", mobile_click))

#using JS we can click on any element directly -- if the link is not clickable directly

driver.execute_script("arguments[0].click();", mobile_click)

#check title
title = driver.execute_script("return document.title;")
print(title)

#refresh the page
# driver.execute_script("history.go(0);")

#generate an alert
#driver.execute_script("alert('Hello');")

#scroll to the bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#scroll to the top of the page
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

#scroll to the point where i can see "Question and Answers"
QnA= driver.find_element(By.XPATH, "//span[text()='Question and Answers']")
driver.execute_script("arguments[0].scrollIntoView();", QnA)


#what kind of browsers we have
print(driver.execute_script("return navigator.userAgent;"))


#check for putting the values in input field with js

input("Enter to exit")




