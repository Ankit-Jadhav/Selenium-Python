'''✅ What Is Constructor Overloading?
🧠 Overloading means same function name, but different number or type of arguments.

👉 But in Python, unlike Java or C++, true constructor overloading is not supported.

🔸 Why?
Because Python does not allow multiple __init__ methods in a class. If you define it twice, the last one overrides the first.'''

# ✅ Simulating Constructor Overloading with default or *args:

class Example:
    def overloading1(self, name = "Ankit"):
        self.name = name
        print(name)

example1 = Example()
example1.overloading1()
example1.overloading1("Aniket")



'''# ✅ What Is Method Overriding?
🧠 Overriding means:
A child class changes the behavior of a method that it inherited from a parent class.'''

class Parent:
    def greeting1(self, name):
        self.name = name
        print("Good Morning", name)

class Child(Parent):
    def greeting1(self, name = None):      # Overriding parent method
        if name:
            print("Good Morning", name)
        else :
            print("Good Afternoon")

obj = Child()
obj.greeting1("Ankit")
obj.greeting1()



# In context of selenium
class baseClass:
    def __init__(self,driver = None):
        self.driver = driver
    def openUrl(self, url):
        self.url = url
        self.driver.get(url)

class GoogleTest(baseClass):
    def openUrl(self, url):                #overriding
        print("Opening Google only")
        return super().openUrl(url)

#start browser
driver = webdriver.Chrome()
obj1 = GoogleTest(driver)
obj1.openUrl("https://www.google.com")


"""✅ Your code is correct and well-structured! It demonstrates:

Class inheritance
Constructor with default value

Method overriding

Use of **super()** to call the parent class method"""