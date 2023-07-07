#The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables). 
#The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

# Defining a function called add_five that takes a parameter x.
def add_five(x):
    # The function adds 5 to the given value of x and returns the result.
    return x + 5

# Creating a list of numbers.
nums = [11, 22, 33, 44, 55]

# Applying the add_five function to each element in the nums list using the map() function.
# The map() function takes two arguments: the add_five function and the nums list.
# It applies the add_five function to each element in the nums list and returns an iterable.
# Converting the iterable to a list using the list() function and assigning the result to the variable result.
#To convert the result into a list, we used list explicitly.
result = list(map(add_five, nums))

# Printing the result, which is a list containing the result of applying the add_five function to each element in the nums list.
print(result)


print("******************************")
#We could have achieved the same result more easily by using lambda syntax.
# Creating a list of numbers.
nums = [11, 22, 33, 44, 55]

# Applying a lambda function to each element in the nums list using the map() function.
# The lambda function takes a parameter x and returns x + 5, adding 5 to each element.
# The map() function takes two arguments: the lambda function and the nums list.
# It applies the lambda function to each element in the nums list and returns an iterable.
# Converting the iterable to a list using the list() function and assigning the result to the variable result.
result = list(map(lambda x: x + 5, nums))

# Printing the result, which is a list containing the updated values after adding 5 to each element in the nums list.
print(result)

#To convert the result into a list, we used list explicitly.

print("*****************************")

