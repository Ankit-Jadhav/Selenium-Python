import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://classic.crmpro.com/")

my_wait = WebDriverWait(driver, 10)
#my_wait.until(ec.title_is("Free CRM software for customer relationship management, sales, and support."))
my_wait.until(ec.title_contains("CRM software"))
print(driver.title)   #for title we have to give explicit wait because it is not cover under implicit wait

input("Exit")


'''
🔍 Explicit Wait is actually dynamic, not static.
✅ Explicit Wait (what you're using):
Dynamic in nature — it will wait only as long as needed, up to the maximum timeout.

Example:
WebDriverWait(driver, 10).until(ec.title_contains("CRM software"))

If the condition is met in 2 seconds, it continues immediately.

If not met in 10 seconds, it throws a TimeoutException.

❌ Static Wait:
A true static wait is when you use something like:

python
Copy
Edit
time.sleep(10)  # Always waits 10 seconds regardless
This is what people often wrongly associate with "explicit wait".

✅ Implicit Wait:
Also dynamic, but works globally and only for finding elements.

If an element is not immediately found, Selenium will poll until the timeout is reached or the element appears.

Example:

python
Copy
Edit
driver.implicitly_wait(10)
🔁 Summary:
Type	        Dynamic/Static	   Scope	         Stops Early if Condition Met?
time.sleep()	Static	           Whole script	            ❌ No
Implicit Wait	Dynamic	           For all element lookups	✅ Yes
Explicit Wait	Dynamic        	   For specific condition	✅ Yes

time.sleep(10) is not part of Selenium's explicit or implicit wait mechanisms. It is a:
⚠️ Static Wait — and it's a basic Python delay, not a Selenium-specific wait.
'''