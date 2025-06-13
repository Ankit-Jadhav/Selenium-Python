import time


from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



#certificate is expired
#method 1
options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver= webdriver.Chrome(options=options)

#method 2
# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True
#driver= webdriver.Chrome(desired_capabilities = desired_capabilities)


#method 3
# options = Options()
# options.set_capability('acceptInsecureCerts', True)
# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://expired.badssl.com/")
print(driver.find_element(By.TAG_NAME, "h1").text)

input("Enter to exit")