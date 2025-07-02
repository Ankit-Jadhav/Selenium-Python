from selenium import webdriver
from selenium.webdriver.common.by import By

#Class  - Defining class(blueprint)
class GoogleSearchTest:

    #Constructor to initalize the browser
    def __init__(self):
        self.driver = webdriver.Chrome()     #Open chrome browser
         # 🔒 Data is inside the class
    
    # Method to open google
    def open_google(self):
        self.driver.get("https://app.hubspot.com/login")    # 🔐 Behavior inside class

    #Method to input email
    def search(self, keyword):
        search_box = self.driver.find_element(By.ID, "username")
        cta_next = self.driver.find_element(By.XPATH, "//button[@data-test-id='password-login-button']")
        search_box.clear()
        search_box.send_keys(keyword)
        cta_next.click()
    

# 🛠️ Create an object of the class
test = GoogleSearchTest()

# 🏃‍♂️ Use the object to call methods
test.open_google()
test.search("check@gmail.com")


input("enter to exit")



'''🧠 Basic Concept
✅ What is a Class?
A class is like a blueprint. It defines how something should behave — in our case, a test or browser session.

Think of a class as a recipe — it doesn’t cook anything itself, but it tells you how to cook.

✅ What is an Object?
An object is the actual thing created from the class (blueprint). It’s like cooking using the recipe.


✅ Your code looks great and is correctly structured for a beginner-friendly Selenium test using classes and objects. You've:

Properly used a class to encapsulate behavior.

Defined a constructor using __init__() to launch the browser.

Created methods for open_google() and search() actions.

Used correct locators (By.ID and By.XPATH).

Called clear() and send_keys() correctly.

Created an object and called methods on it.

Added input("enter to exit") to keep the browser open, which is useful during debugging.

🧠 What is Encapsulation in Python?
Encapsulation means:

Wrapping data (variables) and code (methods) together in a class.

Hiding internal details from outside interference (using private variables/methods).

Controlling access through methods (getters/setters) or public interfaces.

✅ How Your Script Uses Encapsulation (Already):
Your class GoogleSearchTest encapsulates:

Data: the browser (self.driver)

Behavior: actions like opening the site and searching

➡️ These are grouped inside a class, which is the first step of encapsulation.
🧪 Why Encapsulation Matters in Selenium Tests
Encapsulation helps you:

Hide browser logic and locator details from test scripts

Keep the code organized and reusable

Make the test framework robust (if something changes, only one class needs updating)



#Constructor : ✅ What is a Constructor in Python?
A constructor is a special method in a class that gets automatically called when you create an object of the class.
In Python, the constructor method is always named __init__().

🧠 Think of it like:
When you build (construct) a house (object), the constructor sets up the foundation — doors, windows, walls — everything needed to start using it.

#Syntax of constructor : 
class MyClass:
      def __init__(self):   #constructor
          print("Constructor is called")
obj1 = MyClass()   #Output :  Constructor is called!

The __init__() method automatically runs and opens a Chrome browser.

The driver is stored inside the class as self.driver so other methods can use it.


# Instance : 
What is an Instance?
An instance is just another word for an object created from a class.

📦 Think of:
A class is like a blueprint for a car,
An instance is the actual car you build from that blueprint.

class Car:
    def __init__(self):
        print("Car created!")

car1 = Car()   # car1 is an instance of class Car
car2 = Car()   # car2 is another instance


# What is an Instance Variable?
An instance variable is a variable that belongs to the object (instance), not to the class itself.
It is defined using self
Each object can have different values for instance variables.

class car:
   def __init__(self,brand):
       self.brand = brand    # 🔹 instance variable
car1 = car("Honda")
print(car1.brand)

Here, brand is an instance variable, and each object has its own copy.

# What is self?
self refers to the current object (instance) of the class.

It is used to access instance variables and methods from inside the class.

It's mandatory as the first argument in all class methods (even though you don't pass it explicitly when calling the method).



| Term              | Meaning                                                               |
| ----------------- | --------------------------------------------------------------------- |
| Instance          | Object created from a class (`obj = ClassName()`)                     |
| Instance Variable | Variable that belongs to an object (`self.driver`, `self.name`, etc.) |
| `self`            | Refers to the current object inside class methods                     |


'''
