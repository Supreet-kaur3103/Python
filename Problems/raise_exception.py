#You can throw (or raise) exceptions when some condition occurs. 
#For example, when you take user input that needs to be in a specific format, you can throw an exception when it does not meet the requirements.
#This is done using the raise statement.
num = 102

if num > 100:
    raise ValueError("ValueError raised")  # Raising a ValueError with a custom error message.

# Explanation:
# The code checks if the value of `num` is greater than 100.
# If the condition is true, it raises a ValueError using the `raise` keyword.

# In this case, since `num` is 102 (which is greater than 100), the condition is true,
# and a ValueError is raised with the error message "ValueError raised".

# Raising an exception allows you to signal that something unexpected or invalid has occurred
# and can be used to handle exceptional cases in your code.
# When an exception is raised, the normal flow of the program is disrupted,
# and the program jumps to the nearest exception handler (if present) to handle the raised exception.


print("*"*40)
#Exceptions can be raised with arguments that give detail about them.
name = "123"

raise NameError("Invalid name!")  # Raising a NameError with a custom error message.

# Explanation:
# The code raises a NameError using the `raise` keyword and provides a custom error message.

# In this case, the NameError is raised with the error message "Invalid name!".

# Raising an exception allows you to signal that something unexpected or invalid has occurred
# and can be used to handle exceptional cases in your code.
# When an exception is raised, the normal flow of the program is disrupted,
# and the program jumps to the nearest exception handler (if present) to handle the raised exception.


print("*"*40)
