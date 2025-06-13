from selenium import webdriver
import time

def test_google():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    print("Chrome opened")
    chrome_driver.get("https://www.google.com")
    assert chrome_driver.title == "Google"

def test_flipkart():
    edge_driver = webdriver.Edge()
    edge_driver.implicitly_wait(5)
    edge_driver.maximize_window()
    print("Edge opened")
    edge_driver.get("https://www.flipkart.com")
    assert edge_driver.title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"



