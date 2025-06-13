from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.drivers.firefox import GeckoDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserName = "Chrome"

if browserName == "Chrome":
    #for headless
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
elif browserName == "Firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
elif browserName == "Brave":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
elif browserName == "Edge":
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

else:
    raise Exception(f"Invalid browser name: {browserName}")

driver.implicitly_wait(5)

driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, "username").send_keys("a30101996j@gmail.com")
driver.find_element(By.ID, "loginBtn").click()
print(driver.title)

time.sleep(5)
driver.quit()





