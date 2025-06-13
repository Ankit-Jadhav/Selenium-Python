from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/30-day-free-trial")

#click on "book a free demo"
driver.find_element(By.LINK_TEXT, "Book a Free Demo").click()

select_country = driver.find_element(By.ID, "Form_getForm_Country")
select_employees = driver.find_element(By.ID, "Form_getForm_NoOfEmployees")


def dropdown_function(element,value):

    pick = Select(element)
    pick.select_by_visible_text(value)


dropdown_function(select_country,"India")
dropdown_function(select_employees,"< 10" )


all_list = (Select(select_country)).options

for i in all_list:
    print(i.text)
    print(len(all_list))
    
    if i.text =="India":
        i.click()
        break
