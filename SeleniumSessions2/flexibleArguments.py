'''#What are *args and **kwargs in Python?
These are used when you don’t know in advance how many arguments will be passed to a function or method.

| Syntax     | Description                           | Example Value Inside                  |
| ---------- | ------------------------------------- | ------------------------------------- |
| `*args`    | Collects **positional arguments**     | `('email', 'password')`               |
| `**kwargs` | Collects **keyword arguments** (dict) | `{'id': 'username', 'type': 'input'}` |

*args    → A tuple of extra unnamed values
**kwargs → A dictionary of extra named values'''

def sum1(*args):
    print(args)
    total = sum(args)
    print("Total: ", total)

sum1(3,4,5)

def keyValue1(**kwargs):
    print(kwargs)                    # kwargs is a dictionary

    for key, value in kwargs.items():
        print(f"{key}:{value}")


keyValue1(name= "Ankit", age = 25 )

#both

class flexibleArgs:
    def __init__(self):
        pass
    
    def demo_funct1(self, *args, **kwargs):
        print(args)
        print(kwargs)

obj1 = flexibleArgs()

obj1.demo_funct1(1,2,3,"Ankit", age = 25)