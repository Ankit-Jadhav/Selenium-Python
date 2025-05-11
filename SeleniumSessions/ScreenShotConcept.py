import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")


driver= webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)


driver.get("https://www.wikipedia.org/")
#driver.get_screenshot_as_file('screenshot.png')

#full screenshot
#make sure you are running in headless mode
S = lambda X:driver.execute_script('return document.body.parentNode.scroll'+ X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME, 'body').screenshot('screenshotfull.png')

'''
CHATGPT
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Use new headless mode for better rendering
options.add_argument("--window-size=1920,1080")  # Set a large base window size

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://www.wikipedia.org/")
time.sleep(3)  # Let the page load completely

# Use JavaScript to get full scrollable height and width
scroll_width = driver.execute_script('return document.body.scrollWidth')
scroll_height = driver.execute_script('return document.body.scrollHeight')

# Resize the window to capture the entire page
driver.set_window_size(scroll_width, scroll_height)
time.sleep(2)  # Allow resize to settle

# Take screenshot of the full page
driver.find_element(By.TAG_NAME, 'body').screenshot('screenshotfull.png')

print("✅ Full screenshot saved as 'screenshotfull.png'")
driver.quit()
'''