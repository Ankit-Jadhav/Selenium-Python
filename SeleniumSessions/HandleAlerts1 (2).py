#Packages
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Setup
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)


driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#Locators


js_alert = "//button[@onclick = 'jsAlert()']"
js_confirm ="//button[@onclick = 'jsConfirm()']"
js_prompt ="//button[@onclick= 'jsPrompt()']"



#Function to handle all the three alert

def handle_alert(button_xpath, description, send_text = None, accept = True):
    print(f"\n--Testing:{description} ---")

    button = driver.find_element(By.XPATH, button_xpath)
    button.click()

    alert = wait.until(EC.alert_is_present())
    print("Alert Text: ", alert.text )

    if send_text:
        alert.send_keys(send_text)
    
    if accept:
        alert.accept()
        print("Action: Accepted")
    
    else:
        alert.dismiss()
        print("Action: Dismissed")

     # Print the result message shown below buttons


    result = driver.find_element(By.ID, "result").text
    print("Result Message: ", result)
    

    

# 1. jsAlert: OK only

handle_alert(js_alert, "JS Alert (OK Only)")

# 2. jsConfirm: OK
handle_alert(js_confirm, "JS Confirm(OK)", accept = True)

# 2. jsConfirm: Cancel
handle_alert(js_confirm, "JS Confirm(Cancel)", accept = False)

# 3. jsPrompt: Enter text and OK
handle_alert(js_prompt, "JS Prompt (Send Text + OK )", send_text = "Ankit", accept = True)

# 3. jsPrompt: Enter text and Cancel
handle_alert(js_prompt, "JS Prompt (Send Text + Cancel )", send_text = "Test Cancel", accept = False)


input("\nPress Enter to exit...")




input("exit")