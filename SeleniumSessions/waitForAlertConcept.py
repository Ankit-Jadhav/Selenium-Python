import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME, 'proceed').click()

#checking the alert to load and then click on ok and print text
my_wait = WebDriverWait(driver, 10)
alert = my_wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()


# To click "No" or "Cancel"
# alert.dismiss()

#checking the link to load
#checking register link

new_register = my_wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Get a new Rediffmail ID' )))
print(new_register.text)
new_register.click()

#checking the input field to load -- visibility of element
first_name = my_wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"input[placeholder ='Enter your full name']")))
first_name.send_keys('<PASSWORD>')

#question : visibility vs presence
input("Exit")

