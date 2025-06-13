#Selenium Notes: 
1. How do you launch a browser using Selenium WebDriver in Python?

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

2. How do you find elements on page

Case1 : Use By ID   ----Unique and stable identifiers 
element = driver.find_element(By.ID, "id")

Case2: Use By NAME   ----Form fields like input or button elements.
element = driver.find_element(By.NAME, "name")

Case3: Use By CLASS NAME    ---When class is unique (avoid when it's common like btn).
element = driver.find_element(By.CLASS_NAME, "class")

Case4: By TAG NAME -----Finding all elements of a specific HTML tag.
element = driver.find_elemsents(By.TAG_NAME, "a")    //Find All links

Case5: By Link Text  ---- Clicking on full link texts.

<a href="/profile">Go to Profile</a>    -- in this case only it works

element  = driver.find_element(By.LINK_TEXT, "Forgot Password?")
assert "Forgot Password?" in element.text, "Link text does not match!"

Case6: By Partial Link Test --- When link text is dynamic or long.
<a href="/profile">Go to Profile</a>   ---in this case only it works

element = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot")

Case7: By CSS Selector  --- Target using  CSS logic

A. use of TAG in CSS selector
driver.find_element(By.CSS_SELECTOR, "tag")

B. use of ID in CSS selector
driver.find_element(By.CSS_SELECTOR, "#id")

C. use of Class in CSS Selector
driver.find_element(By.CSS_SELECTOR, ".class")

D. use of Attribute Selector
driver.find_element(By.CSS_SELECTOR, "tag[attribute_name = 'attribute_value']")

E. use of Combination: Tag + Class + Attribute

<input type="text" class="form-control" id="username">
driver.find_element(By.CSS_SELECTOR, "input.form_control[type = 'text']")

F. Descendant Selector
Finds elements inside another element.

<form id="loginForm">
  <button type="submit">Login</button>
</form>
driver.find_element(By.CSS_SELECTOR, "loginForm > button")

G. Multiple Classes 
<div class="btn primary large">Submit</div>
driver.find_element(By.CSS_SELECTOR, ".btn.primary.large")

H.  Starts With (^=), Ends With ($=), Contains (*=)
<input name="user_email">

driver.find_element(By.CSS_SELECTOR, "input[name*= 'email']")

I. nth-child() or nth-of-type()

<ul>
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>

driver.find_element(By.XPATH, "//ul/li[text()='Two']")

driver.find_element(By.CSS_SELECTOR, "ul li:nth-child(2)")   #Select TWO


J : use of multiple selectors
<input type="text" name="username" class="input-field">

driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='username'].input-field")



Case 8: By XPATH  --Complex or dynamic DOM structures.

A: Relative Xpath
driver.find_element(By.CSS_SELECTOR, "//tagname[@attribute='value']")

B: Text Matching
<button>Login</button>
driver.find_element(By.CSS_SELECTOR, "//button[text()='Login']")

PARTIAL TEXT : 
driver.find_element(By.XPATH, "//button[contains(text(),'Log')]")

C: Indexing in XPath
<input name="username">
<input name="username">

driver.find_element(By.XPATH, "(//input[name='username'])[1]")    #First

3. Print all the links and there text on the page

from selenium import driver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://example.com")
time.sleep(3)

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

link_dict= {}

for link in links:
      text = link.text.strip()
      href = link.get_attribute("href")

      if text and href:
        print(f"{href} & text is {text}")

4. Capture all the images on the page
image_links = driver.find_elements(By.TAG_NAME, "img")
print(len(image_links))

for image in image_links:
     links = image.get_attribute("src)
     # text = image.text.strip()
     text = image.get_attribute("alt")   # Better than .text for images

     print(links "&" text)
    
5. Capture title of the page

Case 1 : 

# Option 1: Actual page title (from <title> tag in <head>)

print(driver.title)
assert "Title" in driver.title, "Title doesn't match"

Case 2 : 

# Option 2: Heading from the body (if any <h1>)

try: 
    h1 = driver.find_element(By.TAG_NAME, "h1")
    print(h1.text)

except:
    print("h1 not found")

6.  Check X path 
<ul>
  <li>
    <div>
      <a href="#">One</a>
    </div>
  </li>
  <li>
    <div>
      <a href="#">Two</a>
    </div>
  </li>
  <li>
    <div>
      <a href="#">Three</a>
    </div>
  </li>
</ul>


 Recommended XPath (generic and safe):
//ul//li//a

links = driver.find_elements(By.XPATH, "//ul//li//a")
for link in links:
    print(link.text)

7. How do you handle dynamic elements with changing IDs or classes?
# Use dynamic XPath or CSS selectors.
Example: //input[contains(@id, 'search')]

<div id="popup-xyz123" class="modal-open-4581">
  <button class="close-btn" data-id="modal-close">×</button>
</div>

driver.find_element(By.XPATH, //div[contains(@id, 'popup-xyz')]//button).click()

8. Use of text in xpath

Case 1 : Exact match using text()
//tagname[text(), "exact_text"]

Case 2 : Partial match using contains(text(), ...)
//tagname[contains(text(), "Partial")]

E.g driver.find_element(By.XPATH, "//button[text()='Close']").click()

9. Use of span or strong tag for text of link 

<a href="/profile">
  <span>Go to Profile</span>
</a>

//a[span[contains(text(),'Go to Profile')]]


driver.find_element(By.XPATH,"//a[span[contains(text(),'Go to Profile')]]" ).click()


10. How do you wait for an element to appear before interacting with it?

# Case 1 : time.sleep()
- A hardcoded delay

import time
time.sleep(5)  # pause for 5 seconds

# Case 2 : Implicit Wait()  
- A global wait once to the driver
- It is applied to all find_element calls
Only for debugging or demonstration purposes.

driver_implicitly_wait(10)   # wait up to 10 seconds for all elements

# Case 3 : Explicit Wait
A conditional wait --  waits for specific condition to be true before proceeding.
Most powerful and recommended way for dynamic elements.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "element")))


# Conditions : 
A. presence_of_element_located
B. visiblity_of_element_located
C. element_to_be_clickable
D. title_contains
E.alert_is_present
F. invisibility_of_element


* Implicit wait applies globally and waits for a max time before throwing NoSuchElementException.

--  WebDriverWait(driver, 10).until(EC.alert_is_present())   -- wait until an alert is present



11. Different explicit wait uses:

# How do you wait until an element becomes clickable?  
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submitBtn")))

# How do you wait until a specific text appears in an element?
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "status"), "Success"))

# How do you wait until an alert is present?
WebDriverWait(driver, 10).until(EC.alert_is_present())

---visibility_of_element_located

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-msg"))
)


12. Assert the output 

# Below is hard assertion
assert "expected_result" in driver.title, f"Title does not match! the actual title: {driver.title}"

# To avoid crashing the script on failure and still print messages, wrap it in try-except:

try:
    assert "Expected_title" in driver.title, f"Actual and Expected title doesn't match ! Got{driver.title}"
    print("title matches")
except AssertionError as e:
    print(e)


13. Hard Assertion vs Soft Assertion

# Soft Assertion : check.is_in(expected_substring,actual_substring,message)
# check.equal(expected, actual, message)
# check.is_true(condition, message)


-- For element text contains expected value - like title url etc.
check.is_in("Dashboard",driver.title, "Title should contains 'Dashboard'")

--Exact match between actual and expected value
check.equal("Success",driver.find_element(By.ID,"username").text,"username does not match")

--Check visibility, button enablement, checkbox selection.
check.is_true(driver.find_element(By.ID, "submit").is_enabled(), "Submit button should be enabled")
check.is_true(driver.find_element(By.ID, "terms").is_selected(), "Terms checkbox should be selected")
check.is_true(driver.find_element(By.ID, "logout").is_displayed(), "Logout link is not visible")

In the case of important checks like integration methods, we should use hard assertions. For independent verifications or when checking every element on a page, we should use soft assertions.

14. How do you handle JavaScript alerts in Selenium?
alert = driver.switch_to.alert
print(alert.text)
alert.accept
alert.dismiss()
alert.send_keys("test")
Note: If the alert is not present yet, it will throw a NoAlertPresentException.


# use of explicit wait in alert
alert = WebDriverWait(driver,10).until.(EC.alert_is_present)
print(alert.text)

15. Handling HTTP Auth Popups in Selenium with URL
url = f"https://{username}:{password}@{host}"
driver.get(url)

16. Back, Forward and Refresh in selenium
driver.back()
driver.forward()
driver.refresh()

17. Bypass SSL Certificate errors

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options = options)


18. Handle Cookies in Selenium
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

for cookie in cookies:
    print(cookie)


# Add cookiess
driver.add_cookie({"name":"Python", "value":"123ghb"})

# Delete specific cookie
driver.delete_cookie("Python")

# Delete All cookies
delete.delete_all_cookies()

19. Drag and drop script using Selenium + Python

from selenium.webdriver.common.action_chains import ActionChains

# Switch to iframe that contains draggable/droppable elements
element = driver.find_element(By.CLASS_NAME, "demo-frame")
drive.switch_to.frame(element)

drag_me = driver.find_element(By.ID, "draggable")
drop_here = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
actions.drag_and_drop(drag_me,drop_here).perform()


#drag and drop without using drag_and_drop method
#click --- hold --- move element
act_chains.click_and_hold(drag_me).move_to_element(drop_here).perform()


20. Selenium Dropdown Handling in Python

# Basic Dropdown Handling (Single Select)
from selenium.webdriver.support.select import 
element = driver.find_elements(By.ID, "dropdown_id")
select = Select(element)
select.select_by_visible_text("India)
select.select_by_index(2)
select.select_by_value("IN")

# Check if Dropdown is Multiselect
select.is_multiple()

# Deselect Options (Only for Multi-select)
select.deselect_all()
select.deselect_by_value("value")
select.deselect_by_visible_text("text")
select.deselect_by_index(3)


# Print all dropdown options
options = select.options
print(len(options))
for opt in options:
    print(opt.text)

# Select Dropdown Without Using Select Class

options = driver.find_elements(By.XPATH, '//select[@id = "iidi"]/option')
print(len(options))
for opt in options:
   if opt.text =="india";
       opt.click()
       break

# Generic Functions:
def select_dropdown_by_text(element, value):
    for option in element:
        if option.text == value:
            option.click()
            break

# Select all values
options = driver.find_elements(By.XPATH, '//select[@id="yourDropdownId"]/option')
for opt in options:
    opt.click()  # Only works if dropdown allows multiple selections


21. Use of clear

username = driver.find_element(By.ID, "username")
username.clear()  # Clear old input
username.send_keys("Ankit")

22. File Upload in Selenium
<input type="file" name="file_upload">

driver.find_element(By.NAME, "file_upload").send_keys("C:/path/to/file.pdf")





