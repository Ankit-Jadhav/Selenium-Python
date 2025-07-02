import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/alerts.html#")
my_wait = WebDriverWait(driver, 10)


#1. only alert 
alert1 = driver.find_element(By.ID, "alert")
alert1.click()
alertwait = my_wait.until(EC.alert_is_present())
#Switch to alert
alert = driver.switch_to.alert
print(f"text : {alert.text}")
alert.accept()


#2. confirm yes no
alert2 = driver.find_element(By.LINK_TEXT, "test confirm")
alert2.click()
alertwait = my_wait.until(EC.alert_is_present())
confirm = driver.switch_to.alert
print(f"text : {confirm.text}")
confirm.dismiss()
#confirm.accept()


#3. Prompt
alert3 = driver.find_element(By.CSS_SELECTOR, "a[onclick ='displayPrompt();']")
alert3.click()
alertwait = my_wait.until(EC.alert_is_present())
prompt =driver.switch_to.alert
print(f"text : {prompt.text}")
prompt.send_keys("HI")
prompt.accept()

input("enter to exit")



'''# Clear default by sending empty string, then custom text
alert.send_keys("")  # This clears it
alert.send_keys("Ankit Jadhav")  # Type your input'''