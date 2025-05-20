import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.freshworks.com/")
my_wait = WebDriverWait(driver, 10)
#elements to check
footer_links = my_wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.sc-6293d692-0.eNMhGa')))
print(len(footer_links))
for i in footer_links:
    print(i.text)

#for dropdown value ,checkbox
#my_wait(ec.element_to_be_selected('checkbox'))
#for url
#my_wait(ec.url_contains('freshworks'))