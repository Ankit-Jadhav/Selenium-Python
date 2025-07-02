import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Open page with dropdown
driver.get("https://demo.guru99.com/test/newtours/register.php")

dropdown1 = driver.find_element(By.NAME, "country")
select = Select(dropdown1)
options1 = select.options
print(len(options1))

select.select_by_index("1")

time.sleep(5)
select.select_by_value("ANDORRA")

time.sleep(5)
select.select_by_visible_text("ANGUILLA")

option_list = []

for option in options1:
    text = option.text.strip()
    option_list.append(text)
print(option_list)

input("enter to exit")

