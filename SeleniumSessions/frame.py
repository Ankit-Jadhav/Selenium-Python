#frame & Iframe
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.londonfreelance.org/courses/frames/index.html")
time.sleep(5)

#method 1 - Using the index
#driver.switch_to.frame(2)    #2 is the index of frame which we are targeting....means 3rd frame

#index may get shifted if new frame is introduced in between

#method 2 -- Using the id
#driver.switch_to.frame("main")

#method 3 -- By creating a frame element
frame_element = driver.find_element(By.NAME, "main")
driver.switch_to.frame(frame_element)


title_value = driver.find_element(By.CSS_SELECTOR, "body>h2")
print(title_value.text)

#move back to page source
driver.switch_to.default_content()
driver.switch_to.parent_frame()     #for multiple frames



input("Please enter to exit")