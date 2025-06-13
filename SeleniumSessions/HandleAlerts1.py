#Packages
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

#URL
driver.get("https://the-internet.herokuapp.com/javascript_alerts")


#Case 1: Alert only
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
alert1= driver.switch_to.alert
print(alert1.text)
driver.switch_to.alert.accept()

time.sleep(5)


#Case 2: Confirm only
driver.find_element(By.XPATH, "//button[@onclick = 'jsConfirm()']").click()
alert= wait.until(EC.alert_is_present())
print(alert.text)

alert.accept()
#alert.dismiss()


#Case3: Send_Keys
driver.find_element(By.XPATH, "//button[@onclick = 'jsPrompt()']").click()
alert = wait.until(EC.alert_is_present())
print(alert.text)

alert.send_keys("Ankit")
alert.accept()







input("Exit")



