import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/30-day-free-trial")
print(driver.title)

#ID use
username_url= driver.find_element(By.ID, "Form_getForm_subdomain")
fullname= driver.find_element(By.ID, 'Form_getForm_Name')
business_email = driver.find_element(By.ID, 'Form_getForm_Email')
phone_no = driver.find_element(By.ID, 'Form_getForm_Contact')

#link use
privacy_policy_link = driver.find_element(By.LINK_TEXT, 'Privacy Policy.')




username_url.send_keys("AniketCheck3010")
fullname.send_keys("Aniket")
business_email.send_keys("a30101996j@gmail")
phone_no.send_keys('9175198855')
privacy_policy_link.click()


time.sleep(30)





