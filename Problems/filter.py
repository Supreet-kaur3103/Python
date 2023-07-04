#The function filter filters an iterable by leaving only the items that match a condition (also called a predicate).
# Creating a list of numbers.
nums = [11, 22, 33, 44, 55]

# Applying a lambda function to each element in the nums list using the filter() function.
# The lambda function takes a parameter x and checks if x is divisible by 2 (even number) using x % 2 == 0.
# The filter() function takes two arguments: the lambda function and the nums list.
# It applies the lambda function to each element in the nums list and returns an iterable with only the elements that satisfy the condition.
# Converting the iterable to a list using the list() function and assigning the result to the variable res.
res = list(filter(lambda x: x % 2 == 0, nums))

# Printing the res, which is a list containing the elements from nums that are divisible by 2 (even numbers).
print(res)

#Like map, the result has to be explicitly converted to a list if you want to print it.