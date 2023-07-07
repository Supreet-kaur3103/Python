#Functional programming is a style of programming that (as the name suggests) is based around functions. 
#A key part of functional programming is higher-order functions. Higher-order functions take other functions as arguments, or return them as results.

#The function apply_twice takes another function as its argument, and calls it twice inside its body.
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

#     +-----------------------+
#     |       Start           |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |   apply_twice          |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |    func(func(arg))    |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       func(arg)       |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       add_five(x)     |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       return x + 5    |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       return 10 + 5   |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       func(15)        |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       add_five(x)     |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       return x + 5    |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       return 15 + 5   |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |       print(20)       |
#     +-----------------------+
#               |
#               v
#     +-----------------------+
#     |        End            |
#     +-----------------------+



print("******************************************")
#The code defines a function `test` that applies a given function twice to an argument, and it demonstrates this by calling `test` with the `mult` function (which squares a number) and the argument `2`, resulting in the output of `16`.
def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))


print("******************************************")
#Pure Functions 
#Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that depends only on their arguments.
#This is how functions in math work: for example, the cos(x) will, for the same value of x, always return the same result.
#Below are examples of pure and impure functions.
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

#Impure function:
some_list = []

def impure(arg):
  some_list.append(arg)

#The function above is not pure, because it changed the state of some_list.

#Using pure functions has both advantages and disadvantages. 
#Pure functions are:
#- easier to reason about and test.
#- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
#- easier to run in parallel.