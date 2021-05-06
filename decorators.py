# decorators are used to modify a function
# Takes functions as inputs and returns a modified version as an output
def announce(f):
        def wrapper():
            print("About to run the function...")
            f()
            print("Here is the modified version of your function")
        return wrapper

"""
Adding the decorator announce in  this case:
"""
@announce
def hello():
    print("HeloWorld")

"""
executing the function
"""
hello()

# decorators can be used all over the program once they are defined
@announce
def welcome():
    print("Welcome to YWCA")
welcome()

# creating another decorator
def python(f):
    def wrapper():
        print("Hello PythonWorld")
        f()
        print("Python is Great")
    return wrapper

@python
def learn():
    print(" We are learning decorators")
learn()
