import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.csm-testcenter.org/test?do=show&subdo=common&test=file_upload")
time.sleep(5)

#note : type = file attribute should be there then it will work
driver.find_element(By.NAME, "file_upload").send_keys('C:/Users/Ankit Jadhav/OneDrive - CIMET/Desktop/Rest API.pdf')
driver.find_element(By.NAME, "http_submit").click()






input("Exit...")