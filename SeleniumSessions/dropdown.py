import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.orangehrm.com/30-day-free-trial")
driver.implicitly_wait(10)


#dropdown select option using id,select and select_by_visible_text etc...
country_dropdown = driver.find_element(By.ID, "Form_getForm_Country")
select = Select(country_dropdown)
#select.select_by_visible_text("India")
#select.select_by_index(2)

#using the value tag
#select.select_by_value("India")

#how to check the dropdown is multiselect or not
print(select.is_multiple)   

#deselect the values also there opposite of select


#how will you handle the multiple dropdowns at one time.-- use of function
driver.find_element(By.LINK_TEXT, "Book a Free Demo").click()    #click on book a free demo button

def dropdown_function(element, value):
    pick = Select(element)
    pick.select_by_visible_text(value)

select_country = driver.find_element(By.ID, "Form_getForm_Country")
select_employees = driver.find_element(By.ID, "Form_getForm_NoOfEmployees")

dropdown_function(select_country,"India")
dropdown_function(select_employees,"< 10")


# Print all the options of dropdown and then click on one specific option.
pick1= Select(select_country)
Country_list= pick1.options

for i in Country_list:
    print(i.text)
    if i.text == "Australia":
        i.click()
        break

# select the dropdown without using select class
employee_options= driver.find_elements(By.XPATH, '//select[@id="Form_getForm_NoOfEmployees"]/option')
print(len(employee_options))
for i in employee_options:
    print(i.text)
    if i.text =="51 - 200":
        i.click()

# use of function for the above dropdown click -- generic method
def dropdown_function1(dropdown_name, value_to_select):
    print(f"length of options is {len(dropdown_name)}")
    for u in dropdown_name:
        print(u.text)
        if u.text ==value_to_select:
            u.click()
            break


dropdown_employee = driver.find_elements(By.XPATH, '//select[@id="Form_getForm_NoOfEmployees"]/option')
dropdown_country = driver.find_elements(By.XPATH, '//select[@id="Form_getForm_Country"]/option')


dropdown_function1(dropdown_employee,"200 - 1,000")
dropdown_function1(dropdown_country,"American Samoa")









input("Please enter to exit..")


