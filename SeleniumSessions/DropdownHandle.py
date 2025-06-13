import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)



def myfunction_dropdown(dropdown_name, choices):
    for i in dropdown_name:
        print(i.text)
        if i.text == choices:
            i.click()
            break

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(5)
driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(5)
dropdown_one= driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
#choices_one = "choice 6 2 3"

myfunction_dropdown(dropdown_one, "choice 6 2 3")
myfunction_dropdown(dropdown_one, "choice 6 1")








input("Press enter to EXIT...")
