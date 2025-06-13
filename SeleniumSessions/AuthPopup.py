from selenium import webdriver

driver = webdriver.Chrome()

username = "admin"
password = "admin"
host = "the-internet.herokuapp.com/basic_auth"


url =f"https://{username}:{password}@{host}"
driver.get(url)

