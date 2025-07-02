from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-schedule/upcoming-series/league")
wait = WebDriverWait(driver, 10)

#wait until scorboard section loads
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"container" )))

#find all matches
matches = driver.find_elements(By.XPATH, "//div[@itemscope and @itemtype = 'http://schema.org/SportsEvent']")

for match in matches:
    print(match.text)
    print("-" * 60)


# Find all match blocks that contain the word "Dallas" anywhere in their visible text
dallas_matches = driver.find_elements(By.XPATH, "//div[@itemscope and @itemtype='http://schema.org/SportsEvent'][contains(., 'Dallas')]")

# Print text of each match in Dallas
for match in dallas_matches:
    print(match.text)
    print("-" * 60)
