#will write fixtures here - You can offload WebDriver setup/teardown to conftest.py and use it in both BaseTest or directly in tests.
import pytest
from selenium import webdriver

@pytest.fixture(scope = "function")
def driver():
    print("\n[Setup] Launching the browser...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("\n[Teardown] Closing browser...")
    driver.quit()