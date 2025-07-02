from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.hubspot.com/")


#Find all buttons on the page
buttons = driver.find_elements(By.TAG_NAME, "button")

#Create an empty list
button_texts = []

for button in buttons:
    raw_text = button.text                      # Get raw button text
    clean_text = "".join(raw_text.split())      # Remove extra spaces and newlines
    
    if clean_text:                                # Only add if not empty
        button_texts.append(clean_text)

#print final list
print(button_texts)


input("enter to exit")