#You have already seen exceptions in previous code. They occur when something goes wrong, due to incorrect code or input. When an exception occurs, the program immediately stops.
#The following code produces the ZeroDivisionError exception by trying to divide 7 by 0: 
#An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program.
num1 = 7
num2 = 0

# The code will raise a ZeroDivisionError because dividing any number by zero is undefined.

print(num1/num2)

print("*"*40)
#To fix the above code
num1 = 7
num2 = 0

# Adding exception handling to handle the ZeroDivisionError
try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
#or the other way is
try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")
    
#Different exceptions are raised for different reasons. 
#Common exceptions:
#ImportError: an import fails;
#IndexError: a list is indexed with an out-of-range number;
#NameError: an unknown variable is used;
#SyntaxError: the code can't be parsed properly; 
#TypeError: a function is called on a value of an inappropriate type;
#ValueError: a function is called on a value of the correct type, but with an inappropriate value.

print("*"*40)
#A try statement can have multiple different except blocks to handle different exceptions.
#Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
try:
    variable = 10
    print(variable + "hello")  # This line will raise a TypeError due to concatenating a string with an integer.
    print(variable / 2)  # This line will raise a TypeError because dividing an integer by a string is not valid.
except ZeroDivisionError:
    print("Divided by zero")  # This block will not be executed since there is no ZeroDivisionError raised.
except (ValueError, TypeError):
    print("Error occurred")  # This block will be executed when a ValueError or TypeError is raised.

# Explanation:
# The try-except block is used to catch and handle specific types of exceptions that may occur within the try block.

# In this example, within the try block:
# - The variable `variable` is assigned a value of 10.
# - The line `print(variable + "hello")` attempts to concatenate a string ("hello") with an integer (10),
#   which raises a TypeError since these two types cannot be directly combined.
# - The line `print(variable / 2)` attempts to divide the integer `variable` by 2, but since the previous line
#   already raised a TypeError, this line also raises a TypeError since dividing an integer by a string is invalid.

# Since both lines within the try block raise TypeErrors, the except block that catches ValueError and TypeError is executed.
# The message "Error occurred" will be printed to indicate that an error of either ValueError or TypeError occurred.
# The ZeroDivisionError except block will not be executed since no ZeroDivisionError is raised in the try block.

print("*"*40)
#An except statement without any exception specified will catch all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.

try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")
    
    
print("*"*40)
def withdraw(amount):
   print(str(amount) + " withdrawn!")

try:
   withdraw(int(input()))  # Calling the `withdraw` function and passing an input value as the amount.

except(ValueError):
   print("Please enter a number")  # This block will be executed if a ValueError occurs during the conversion to an integer.

# Explanation:
# The `withdraw` function takes an `amount` parameter and prints the amount followed by "withdrawn!".

# In the code, the `withdraw` function is called inside a try-except block.
# The input value is converted to an integer using `int(input())` and passed as the `amount` argument to the `withdraw` function.

# If the conversion to an integer is successful, the `withdraw` function is executed, and the amount is printed with "withdrawn!".
# However, if a ValueError occurs during the conversion (e.g., if the user enters a non-numeric value), the except block is executed.
# The except block prints the message "Please enter a number" to indicate that the user should enter a valid numeric value.


print("*"*40)
#Finally
#After a try/except statement, a finally block can follow. It will execute after the try/except block, no matter if an exception occurred or not.
#The finally block is useful, for example, when working with files and resources: it can be used to make sure files or resources are closed or released regardless of whether an exception occurs.
try:
    print("Hello")  # This line will be executed and print "Hello".
    print(1 / 0)  # This line will raise a ZeroDivisionError.
except ZeroDivisionError:
    print("Divided by zero")  # This block will be executed to handle the ZeroDivisionError.
finally:
    print("This code will run no matter what")  # This block will be executed regardless of whether an exception occurs.

# Explanation:
# The try-except-finally block is used to catch and handle exceptions, and ensure that certain code runs regardless of exceptions.

# In this example:
# - The line `print("Hello")` will be executed and print "Hello" to the console.
# - The line `print(1 / 0)` attempts to divide 1 by 0, which raises a ZeroDivisionError.
# - Since a ZeroDivisionError is raised, the except block that catches ZeroDivisionError is executed,
#   and the message "Divided by zero" is printed to indicate the error.
# - Finally, the finally block is executed, which will always run regardless of whether an exception occurred or not.
#   In this case, it prints "This code will run no matter what".
# - After the finally block executes, the program terminates.

print("*"*40)
#Else
#The else statement can also be used with try/except statements. 
#In this case, the code within it is only executed if no error occurs in the try statement.

try:
    print(1)  # This line will be executed and print "1".
except ZeroDivisionError:
    print(2)  # This block will not be executed since there is no ZeroDivisionError.
else:
    print(3)  # Since there is no exception, this block will be executed and print "3".

try:
    print(1/0)  # This line will raise a ZeroDivisionError.
except ZeroDivisionError:
    print(4)  # This block will be executed to handle the ZeroDivisionError.
else:
    print(5)  # This block will not be executed since there was an exception in the try block.



print("*"*40)
menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

try:
    num = int(input())  # Prompting the user to enter a number.
    print(menu[num])  # Accessing the menu list using the input number as the index.
except IndexError:
    print("Item not found")  # This block will be executed if the input number is out of range for the menu list.
except:
    print("Error occurred")  # This block will be executed for any other exception (e.g., ValueError).
else:
    print("Thanks for your order")  # This block will be executed if no exception occurs.

# Explanation:
# The code allows the user to enter a number and attempts to access the corresponding item in the menu list.

# The try-except-else block is used to catch and handle exceptions.
# - The line `num = int(input())` prompts the user to enter a number and converts it to an integer.
# - The line `print(menu[num])` tries to access the menu list using the input number as the index.

# If the input number is within the valid range of indices for the menu list, the corresponding item will be printed.
# - If the input number is out of range (raises an IndexError), the except block for IndexError will be executed,
#   and the message "Item not found" will be printed.
# - If any other exception occurs (e.g., ValueError when converting input to an integer), the except block
#   without specifying the exception type will be executed, and the message "Error occurred" will be printed.

# If no exception occurs during the try block, the else block will be executed and print "Thanks for your order".
# The else block will not be executed if an exception occurs.

# Note: It's generally recommended to catch specific exceptions rather than using a generic except block.
# This allows for more precise handling of specific exceptions and better error reporting.

print("*"*40)
try:
    print(1)  # This line will be executed and print "1".
    print(1 + "1" == 2)  # This line will raise a TypeError.
    print(2)  # This line will not be executed.
except TypeError:
    print(3)  # This block will be executed to handle the TypeError.
else:
    print(4)  # This block will not be executed since there was an exception in the try block.

# Explanation:
# The code demonstrates the use of the try-except-else structure in exception handling.

# In the try block:
# - The line `print(1)` is executed, and "1" is printed.
# - The line `print(1 + "1" == 2)` attempts to add an integer with a string and compare it to 2.
#   This operation raises a TypeError since adding different types (int and str) is not valid.
# - Since a TypeError is raised, the except block that catches TypeError is executed, and "3" is printed.
# - The line `print(2)` is skipped since there was an exception before it.

# Since there was an exception in the try block, the else block is not executed.
# Therefore, "4" is not printed.

# The output will be:
# 1
# 3
