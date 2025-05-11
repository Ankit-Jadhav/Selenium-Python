import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")
time.sleep(5)

# "move to element"
fashion_element = driver.find_element(By.CSS_SELECTOR, '[aria-label="Fashion"]')    #hover on fashion
act_chains = ActionChains(driver)
act_chains.move_to_element(fashion_element).perform()

men_footwear_element = driver.find_element(By.LINK_TEXT, "Men Footwear")
act_chains.move_to_element(men_footwear_element).perform()

men_casual_footwear_element = driver.find_element(By.LINK_TEXT, "Men's Casual Shoes")
men_casual_footwear_element.click()



input("Please enter to exit")






