import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.freshworks.com/")
driver.implicitly_wait(10)


#Tag name we use for printing the text of title -- because h1 is only one tag we use all the page. this can be a good example
title = driver.find_element(By.TAG_NAME, "h1")
print(title.text)


# Capture total number of links available on the page
#note : all the links associated with a tag on the page
links = driver.find_elements(By.TAG_NAME, "a")

print(f"total links are {len(links)}")
   
for link in links:
    href= link.get_attribute("href") or "No href"
    link_text =link.text.strip()

    #print( link_text +" -> " + href )

    if not link_text and href:
        print("No text -> " , href)
    elif link_text and not href:
        print(link_text, "No href")
    elif link_text and href:
        print(link_text, "href -> ", href)

#capture all the images on the page
images = driver.find_elements(By.TAG_NAME, "img")
print(f"total images are {len(images)}")
for image in images:
    print(image.get_attribute("src"))

input("Please enter to exit....")



