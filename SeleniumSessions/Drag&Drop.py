import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
time.sleep(5)

drop_here = driver.find_element(By.ID, "droppable")
drag_me = driver.find_element(By.ID, "draggable")

#drag and drop using drag_and_drop method
act_chains = ActionChains(driver)
#act_chains.drag_and_drop(drag_me,drop_here).perform()

#drag and drop without using drag_and_drop method
#click --- hold --- move element
act_chains.click_and_hold(drag_me).move_to_element(drop_here).perform()