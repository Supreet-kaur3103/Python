#Decorators provide a way to modify functions using other functions. 
#This is ideal when you need to extend the functionality of functions that you don't want to modify.
def decor(func):
    # Define a new function called wrap that acts as a decorator.
    def wrap():
        # Print a line of equal signs before calling the original function.
        print("============")
        # Call the original function.
        func()
        # Print another line of equal signs after calling the original function.
        print("============")
    # Return the wrap function as the decorated version of the original function.
    return wrap

def print_text():
    # Define a simple function that prints "Hello world!"
    print("Hello world!")

# Decorate the print_text function using the decor decorator function.
# Assign the decorated version of the function to the variable decorated.
decorated = decor(print_text)

# Call the decorated function, which will invoke the wrap function defined inside the decor decorator.
decorated()

print("*****************************")
#another way to write this code is
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

print_text = decor(print_text)

print_text()

print("***********************************************")
#Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
#If we are defining a function we can "decorate" it with the @ symbol like:
# Define the decor function, which takes a function as an argument and returns a decorated version of the function
def decor(func):
    # Define the wrap function, which acts as a decorator and adds additional functionality to the original function
    def wrap():
        # Print a line of equal signs before calling the original function
        print("============")
        # Call the original function
        func()
        # Print another line of equal signs after calling the original function
        print("============")
    # Return the wrap function as the decorated version of the original function
    return wrap

# Use the @decor decorator syntax to decorate the print_text function
@decor
def print_text():
    print("Hello world!")

# Call the decorated print_text function, which will invoke the wrap function defined inside the decor decorator
print_text()

print("*******************************************")
# Define the decor function, which takes a function as an argument and returns a decorated version of the function
def decor(func):
    # Define the wrap function, which acts as a decorator and adds additional functionality to the original function
    def wrap(x):
        # Print three asterisks before calling the original function
        print("***")
        # Call the original function with the provided argument
        func(x)
        # Print three asterisks after calling the original function
        print("***")
        # Print "END OF PAGE" to mark the end of the page
        print("END OF PAGE")
    # Return the wrap function as the decorated version of the original function
    return wrap

# Use the @decor decorator syntax to decorate the invoice function
@decor
def invoice(num):
    # Print the text "INVOICE #" concatenated with the provided number argument
    print("INVOICE #" + num)

# Prompt the user to enter a number and pass it as an argument to the decorated invoice function
invoice(input())
