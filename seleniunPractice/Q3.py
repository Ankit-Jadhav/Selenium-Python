import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/droppable/")
my_wait = WebDriverWait(driver, 10)

# Switch to the iframe first
iframe =my_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame")))
driver.switch_to.frame(iframe)

drag_me = my_wait.until(EC.presence_of_element_located((By.ID, "draggable")))
drop_here = my_wait.until(EC.presence_of_element_located((By.ID, "droppable")))

actions = ActionChains(driver)
actions.drag_and_drop(drag_me, drop_here).perform()

input("enter to exit")
