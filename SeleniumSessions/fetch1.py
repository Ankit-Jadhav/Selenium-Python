from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-schedule/upcoming-series/international")
wait = WebDriverWait(driver, 10)

# Wait for elements to load (optional but good practice)
driver.implicitly_wait(10)

# Find all <a> tags near the location span
match_elements = driver.find_elements(By.XPATH, '//div[@itemscope and @itemtype = "http://schema.org/SportsEvent"][contains(.,"Colombo")]')

for match in match_elements:
    print(match.text)

#//div[@itemscope and @itemtype = "http://schema.org/SportsEvent"][contains(.,"Colombo")]