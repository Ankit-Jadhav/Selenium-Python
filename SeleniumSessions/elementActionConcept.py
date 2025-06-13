import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://classic.crmpro.com/")
time.sleep(5)

username= driver.find_element(By.NAME, "username" )
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.XPATH, "//input[@value='Login']")
# action class use
act_chains = ActionChains(driver)
act_chains.send_keys_to_element(username, "batchAuto")
act_chains.send_keys_to_element(password, "test@123")
#send_keys_to_element this by default using perform()
act_chains.click(login).perform()

input("Enter to exit..")








