import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

#Generic function to select all dropdown values and multiselect.
def function_dropdown(dropdown_names, lists):
    if not lists[0] == "all":
        for k in dropdown_names:
            print(k.text)
            for i in range(len(option_list)):
                   if k.text == lists[i]:
                      k.click()
    else :
        try:
            for k in dropdown_names:
                k.click()
        except Exception as e:
            print(e)


driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(5)
driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(5)
dropdown_one = driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
#option_list = ['choice 2 3','choice 6','choice 6 1']
#if someone is giving me all
option_list = ["all"]

function_dropdown(dropdown_one, option_list)


input("Enter to exist")