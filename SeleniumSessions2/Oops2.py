'''✅ Class
✅ Object
✅ Constructor (__init__)
✅ Inheritance
✅ Encapsulation
✅ Abstraction
✅ Decorator (custom logger)
✅ Method Overloading (Pythonic way)
✅ Method Overriding 

✅ 1. Class
Definition:
A class is a blueprint for creating objects. It defines properties (variables) and behaviors (methods).
Interview Answer:

In Selenium, I use classes to structure each webpage in the Page Object Model. Each class represents a page and contains methods for interacting with its elements.

✅ 2. Object
Definition:
An object is an instance of a class. It allows you to access the class methods and properties.
Interview Answer:

I create objects of page classes in my test scripts to interact with elements. For example, I instantiate LoginPage and call methods like enter_username() and click_login().

✅ 3. Constructor (__init__)
Definition:
The __init__() method initializes the class object with default or required values. It's automatically called when the object is created.

Interview Answer:

I use __init__() in my Selenium classes to pass and store the WebDriver instance so that all methods in that class can use it.
✅ 4. Inheritance
Definition:
Inheritance allows a class to use methods and variables from another class.
Interview Answer:

I use inheritance to create a base class with common Selenium actions like click, send_keys, or wait, and reuse those in all page classes to avoid code duplication.
✅ 5. Encapsulation
Definition:
Encapsulation hides internal variables or logic from being directly accessed. In Python, we use _ or __ to indicate protected/private members.
Interview Answer:

Encapsulation helps me secure and organize code better. I use private variables for sensitive data like passwords and expose only getter or setter methods when needed.
✅ 6. Abstraction
Definition:
Abstraction means hiding unnecessary internal details and exposing only essential functionality.
Interview Answer:

I use abstraction in Selenium to define a common interface for all page classes using abstract base classes. This ensures every page implements essential methods like open_url().
✅ 7. Decorator (Custom Logger)
Definition:
A decorator is a function that wraps another function to extend its behavior. Often used for logging or exception handling.
Interview Answer:

I use decorators for custom logging. It helps me trace which test method is running without changing the function logic. It makes debugging easier and improves reports.
✅ 8. Method Overloading (Pythonic way)
Definition:
Python doesn't support method overloading directly. Instead, it’s done using default arguments or *args, **kwargs.
Interview Answer:

I use default parameters to simulate method overloading in Python. It helps create flexible methods that can handle multiple scenarios, such as clicking with or without waits.
✅ 9. Method Overriding
Definition:
Overriding allows a child class to redefine a method from the parent class.
Interview Answer:

I override methods when a page needs extra behavior. For example, a child class can override open_url() from BasePage to log something or perform a check after loading.
| Concept                | Purpose in Selenium                                       |
| ---------------------- | --------------------------------------------------------- |
| Class                  | Represents a page or utility in the framework             |
| Object                 | Used to access class methods and properties               |
| Constructor `__init__` | Initializes driver and variables in page classes          |
| Inheritance            | Promotes code reuse from base to child classes            |
| Encapsulation          | Hides internal data and provides controlled access        |
| Abstraction            | Enforces a structure via abstract base classes            |
| Decorator              | Adds logging/extra behavior without changing core method  |
| Method Overloading     | Achieved with default args; enables flexible method usage |
| Method Overriding      | Customizes parent behavior in child class                 |

✅ What is a Getter and Setter in Python?
Getters and Setters are methods used to access (get) and update (set) the value of private or protected variables.
This supports encapsulation — hiding internal data and exposing only controlled access.

🔐 Why Use Getters and Setters?
To control how a variable is read or modified.
To add validation or logging during get/set.
To hide internal representation of variables.

✅ Interview-Ready Answer:
Getters and setters in Python are used to read and modify private variables. I use them to control how sensitive or internal data is accessed, and often include validation in setters to prevent bad data from being set.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ✅ Decorator to log method start and end
def log_step(func):                                       # Step 1: Accept the function to wrap
    def wrap(*args,**kwargs):                             # Step 2: Define a wrapper that accepts any arguments
        print(f"Start: {func.__name__}")                   # Step 3: Log before function runs
        result = func(*args,**kwargs)                      # Step 4: Call the original function
        print(f"End: {func.__name__}")                     # Step 5: Log after function runs
        return result                                       # Step 6: Return the result of the original function
    return wrap

# ✅ Base class (parent) - shows constructor, encapsulation, overloading

class BaseTest:
    def __init__(self,driver=None):            # ✅ Constructor with overloading style (default param)
        if driver: 
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()     # open browser if driver not given

    def openUrl(self,url):                        # ✅ Encapsulation: internal state controlled through method
        self.driver.get(url)
    
    def close_broswer(self):
        self.driver.quit()


# ✅ Child class - Inherits and overrides method

class GoogleTest(BaseTest):
    
    @log_step
    def openUrl(self, url):          # ✅ Method Overriding + Decorator
        print("Opening Google via overridden method")
        return super().openUrl(url)
    
    @log_step
    def search_google(self,keyword):
        search_box = self.driver.find_element(By.ID, "id")
        search_box.send_keys(keyword)
        search_box.submit()
        time.sleep(2)
 
test = GoogleTest()
test.openUrl("https://www.google.com")
test.search_google("Python Selenium Abstraction")
test.close_browser()



'''
| Concept           | Used in                             | Notes                          |
| ----------------- | ----------------------------------- | ------------------------------ |
| **Constructor**   | `__init__()` in `BaseTest`          | Sets up browser                |
| **Encapsulation** | `self.driver` kept private to class | Not exposed outside            |
| **Inheritance**   | `GoogleTest(BaseTest)`              | GoogleTest uses base setup     |
| **Abstraction**   | `TestBase` (abstract class)         | Forces child to define methods |
| **Overloading**   | `__init__(driver=None)`             | Optional driver argument       |
| **Overriding**    | `open_url` in `GoogleTest`          | Re-defines parent behavior     |
| **Decorator**     | `@log_step`                         | Logs start & end of test steps |
'''



#multiple inheritance

class A:
    def a_method(self):pass
class B: 
    def b_method(self):pass
class Test(A,B):
    def test(self): pass

test = Test()
test.a_method()   # From class A
test.b_method()   # From class B
test.test()       # From class Test

