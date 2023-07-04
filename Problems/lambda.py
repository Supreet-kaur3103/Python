# Defining a function called my_func that takes two arguments: f (a function) and arg (an argument).
def my_func(f, arg):
    return f(arg)
    # The my_func function calls the given function f with the argument arg and returns the result.

# Calling the my_func function with a lambda function as the f argument and 5 as the arg argument.
# The lambda function takes a parameter x and returns the result of 2 * x * x.
# The my_func function applies the lambda function to the argument 5, resulting in the output of 50.
print(my_func(lambda x: 2 * x * x, 5))

# Lambdas are also known as anonymous functions


print("******************************************")
# Named function
def polynomial(x):
    # Defining a named function called polynomial that takes a parameter x.
    return x**2 + 5*x + 4
    # The function computes and returns the value of the polynomial expression.

# Calling the polynomial function with the argument -4.
# The function evaluates the polynomial expression for x = -4, resulting in the output of 0.
print(polynomial(-4))

# Lambda function
# Using a lambda function to define an anonymous function in a single line.
# The lambda function takes a parameter x and returns the value of the polynomial expression.
# Immediately invoking the lambda function by passing -4 as the argument.
# The lambda function is evaluated for x = -4, resulting in the output of 0.
print((lambda x: x**2 + 5*x + 4)(-4))
