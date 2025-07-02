#Basic browser setup fixture
import pytest 
from selenium import webdriver

@pytest.fixture(params= ["chrome", "edge"])
def browser(request):
    browser_name = request.param
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser_name =="edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser : {browser_name}")
    
    driver.maximize_window()
    yield driver
    driver.quit()