from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.google.com")

print(driver.title)
time.sleep(2)

driver.find_element(By.NAME,'q').send_keys("naveen automationlabs")
time.sleep(2)

optionList= driver.find_elements(By.CSS_SELECTOR,'ul.G43f7e li span')
print(len(optionList))
time.sleep(5)
for ele in optionList:
    if ele.text:
        print(ele.text)
time.sleep(2)
for ele in optionList:
    if ele.text =='naveen automationlabs java':
        ele.click()
        break

time.sleep(2)

# driver.quit()

