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
element = driver.find_elements(By.TAG_NAME, "a")    //Find All links

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

| Use Case                   | Correct Method                          | Example                             |
| -------------------------- | --------------------------------------- | ----------------------------------- |
| Check if `a` in `b`        | `check.is_in(a, b)`                     | `check.is_in("Python", "Python 3")` |
| Check if `a == b`          | `check.equal(a, b)`                     | `check.equal(2 + 2, 4)`             |
| Check if `a > b`           | `check.greater(a, b)`                   | `check.greater(10, 5)`              |
| Check if `a is None`       | `check.is_none(a)`                      | `check.is_none(None)`               |
| Check if `a is not None`   | `check.is_not_none(a)`                  | `check.is_not_none("value")`        |
| Check if `a is True/False` | `check.is_true(a)`, `check.is_false(a)` | `check.is_true(5 > 3)`              |

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
case 1 : 
alert = driver.switch_to.alert
print(alert.text)
alert.accept
alert.dismiss()
alert.send_keys("test")
Note: If the alert is not present yet, it will throw a NoAlertPresentException.

case 2: 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//button[@onclick = 'jsConfirm()']").click()  # Click to open confirm box
alert = wait.until(EC.alert_is_present())
print(alert.text)
alert.send_keys("Ankit")
alert.aceept




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
select.select_by_visible_text("India")
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

23. What is ActionChains and why use it for sending keys or clicking?

from selenium.webdriver import ActionChains

username= driver.find_element(By.NAME, "username" )
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.XPATH, "//input[@value='Login']")

# action class use
act_chains = ActionChains(driver)    # You chain the desired actions and then call .perform() to execute them.
act_chains.send_keys_to_element(username, "batchAuto")
act_chains.send_keys_to_element(password, "test@123")

#send_keys_to_element this by default using perform()
act_chains.click(login).perform()

# 🎯 When to use:

When interacting with complex UI elements like sliders, hover menus, or chained keyboard/mouse actions.

📌 You must call .perform() at the end to execute the action.

24. What is the difference between send_keys() and ActionChains.send_keys_to_element()?

# Normal Way
username.send_keys("batchAuto")

# ActionChains
act_chains.send_keys_to_element(usernam,"batchAuto").perform()

🔄 Both work similarly, but ActionChains is useful when you want to chain multiple actions, such as hover + click + type.

25. ActionChains in selenium
ActionChains in Selenium with Python is used to perform advanced user interactions like:

Mouse hover (move_to_element)
Click and hold
Right-click (context click)
Double-click
Drag and drop

26. Hover Over a Menu and Click Submenu

# Hover on 'Account & Lists'
account_list = driver.find_element(By.ID, "nav-link-accountList")
actions = ActionChains(driver)
actions.move_to_element(account_list).perform()

time.sleep(2)  # Wait to see the hover effect

# Click on 'Your Orders' under the hover menu
your_orders = driver.find_element(By.LINK_TEXT, "Your Orders")
your_orders.click()

27. Double Click on an Element
element = driver.find_element(By.ID, "double-click-btn")
actions = ActionChains(driver)
actions.double_click(element).perform()

28. Right Click (Context Click)
element = driver.find_element(By.ID, "right-click-btn")
actions = ActionChains(driver)
actions.context_click(element).perform()

29. Drag and Drop

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

30. Hover and then click on element

# Step 1: Hover over the "Account & Lists" menu
hover_element = driver.find_element(By.ID, "nav-link-accountList")
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()

time.sleep(2)  # Wait to see the dropdown appear

# Step 2: Click on the revealed "Your Orders" option
click_element = driver.find_element(By.LINK_TEXT, "Your Orders")
actions.move_to_element(click_element).click().perform()

# Alternative Syntax (Chain hover and click together):
actions = ActionChains(driver)
actions.move_to_element(hover_element).move_to_element(click_element).click().perform()

📌 Where It's Commonly Used
Mega menus (e.g., Amazon, Flipkart)

Dropdown navigation

Hidden buttons revealed on hover


31. What happens if an element is not found? How do you handle it?

try:
    profile = driver.find_element(By.ID, "profileBtn")
except Exception as e:
    print("Element not found:", e)

32. How to take a screenshot when a test fails?
driver.save_screenshot("login_failure.png")

33. frame and iframe
Both <frame> and <iframe> allow embedding another HTML document within the current one.

34.  How do you interact with elements inside a frame or iframe?
driver.switch_to.frame()

35. What are the different ways to switch to a frame in Selenium?
# index
driver.switch_to.frame(2)  # Switch to the 3rd frame (index starts from 0)

# By Name or ID
driver.switch_to.frame("main")  # Name attribute of the frame

# By Element
frame_element = driver.find_element(By.NAME, "main")
driver.switch_to.frame(frame_element)

#  How do you come out of a frame?
* To return to the main (default) content:
driver.switch_to.default_content()

* To go back to parent frame (in case of nested frames):
driver.switch_to.parent_frame()

36. How to Count All Frames on a Page?

frames = driver.find_elements(By.TAG_NAME, "frame")
print("Total number of frames:", len(frames))

or, iframes
iframes = driver.find_elements(By.TAG_NAME, "iframe")
print("Total iframes:", len(iframes))

37. What is ChromeOptions in Selenium and why is it used?
Answer:ChromeOptions is used to customize or modify the default behavior of ChromeDriver.
📌 Examples of use:
* Run browser in headless mode (no UI)
* Start browser in incognito mode
* Disable notifications, set download path, block popups, etc.

38. How do you combine multiple options like headless + incognito?
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)


39. For CSV refer ReadExcelDDT.py

40. CrossBrowser


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


41. Headless Mode & Full Page Screenshot
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://www.wikipedia.org/")
time.sleep(3)

scroll_width = driver.execute_script("return document.body.scrollWidth")
scroll_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(scroll_width, scroll_height)
time.sleep(2)

driver.find_element(By.TAG_NAME, "body").screenshot("screenshotfull.png")
print("✅ Screenshot saved")

driver.quit()

42. JS Executor

# How do you fetch the full inner text of a webpage using JS Executor?
inner_text = driver.execute_script("return document.documentElement.innerText;")
print(inner_text)

🧠 Use Case:
Extracting the visible text of an entire webpage for debugging or validation.

#  How do you highlight an element using JS for visual debugging?
driver.execute_script("arguments[0].style.border='3px solid red'", element)

🧪 Use Case:
Visually highlight an element before taking a screenshot.
Helps QA find UI issues like overlapping or alignment bugs.

# using JS we can click on any element directly -- if the link is not clickable directly
driver.execute_script("arguments[0].click();", mobile_click)

🎯 Use Case:

Element is hidden behind another
JS-based buttons
Clicks that need bypassing the native click path

# check title
How do you get the page title using JS Executor?
title = driver.execute_script("return document.title;")
print(title)

# How to scroll to the bottom of a page using JavaScript?

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

And scroll to top:

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

# How do you scroll to a specific element (e.g., "Question and Answers")?
QnA = driver.find_element(By.XPATH, "//span[text()='Question and Answers']")
driver.execute_script("arguments[0].scrollIntoView();", QnA)

# How do you generate an alert box using JavaScript?
driver.execute_script("alert('Hello');")

# How do you refresh the page using JavaScript?
driver.execute_script("history.go(0);")
🧠 Can be used if driver.refresh() doesn’t work due to JS-heavy pages.

# How to fetch browser info using JS?
driver.execute_script("return navigator.userAgent;")

✅ This returns browser details like version, OS, etc.

#  How to set value in an input field using JavaScript?
driver.execute_script("arguments[0].value='your_value';", element)
🎯 Bypasses normal send_keys() in case the field is blocked or masked.

# When should you use JavaScriptExecutor over standard Selenium methods?


 | Situation                              | Recommendation             |
| -------------------------------------- | -------------------------- |
| Element is not interactable            | Use JS click               |
| Dynamic scroll issues                  | Use scrollIntoView         |
| Input field doesn’t accept `send_keys` | Use JS to set `.value`     |
| Debugging UI visually                  | Use JS highlight           |
| Page loading or browser info needed    | Use JS to fetch properties |



# Que 43: print links on the page, button text, dropdown, images , list
# Que Save Screenshots
# Fluent wait
# Export CSV


#Que : <div class="match-info">
    <span>IPL 2025</span>
    <div>Match played in Dallas Stadium</div>
</div>

xpath : //div[contains(., 'Dallas')]



This returns all elements anywhere on the page that display the word "Dallas", even inside nested spans, divs, etc.
driver.find_elements(By.XPATH, "//*[contains(., 'Dallas')]")


#Que 

<input type="user_email">
<input type="_user">
<input type="_hhidf_user">


xpath = //input[contains(@type,"user")]


Que: buttons = driver.find_elements(By.TAG_NAME, 'button')

for button in buttons:
    text = button.text.strip()
    button_type = button.get_attribute("type")
    button_id = button.get_attribute("id")
    print(f'Text: "{text}", Type: {button_type}, ID: {button_id}')

print("Total buttons:", len(buttons))


que : check broken links on the page

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

for link in links:
   text = link.text.strip()
   href = link.get_attribute("href")

   if href and href.startswith("http"):
      response = requests.get(href)
      if response.status_code >= 400 :
         print(f"broken links : {href} --> {response.status_code}") 
      else : 
            print(f"working fine {href }")   

Que : broken images on the page

images = driver.find_elements(By.TAG_NAME, "img")
print(len(images))

for image in images:
    text = image.get_attribute("alt")
    src= image.get_attribute("src")
    print(text.strip(), src)
    
    if src and src.startswith("http"):
      response = requests.get(src)
      if response.status_code >=400:
        print(text , src , response.status_code)
      else:
       print(f"{src} valid link")
