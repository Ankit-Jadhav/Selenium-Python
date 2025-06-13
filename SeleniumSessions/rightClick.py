import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(5)

#right/context click
right_click_ele = driver.find_element(By.XPATH, "//span[text()= 'right click me']")
act_chain = ActionChains(driver)
act_chain.context_click(right_click_ele).perform()

right_click_options = driver.find_elements(By.CSS_SELECTOR,'li.context-menu-icon span')
for i in right_click_options:
    print(i.text)
    if i.text == 'Copy':
        i.click()
        break

input("Enter to exit")