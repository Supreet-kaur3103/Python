#Recursion is a very important concept in functional programming. 
#The fundamental part of recursion is self-reference -- functions calling themselves. It is used to solve problems that can be broken up into easier sub-problems of the same type.
#A classic example of a function that is implemented recursively is the factorial function, which finds the product of all positive integers below a specified number. 
#For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!. 
#Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials. 
#Below is a recursive implementation of the factorial function.
def factorial(x):
  # Base case: if x is 1, return 1
  if x == 1:
    return 1
  else: 
    # Recursive case: multiply x with factorial of (x-1)
    return x * factorial(x-1)
    
# Call the factorial function with argument 5
print(factorial(5))


print("**********************************************")
#Recursion can also be indirect. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions.
def is_even(x):
  print(x)  
  # Base case: if x is 0, it is even, so return True
  if x == 0:
    return True
  else:
    # Recursive case: if x is not 0, call is_odd with (x-1)
    return is_odd(x-1)

def is_odd(x):
  # If x is odd, it means it's not even
  # So, return the negation of is_even(x)
  return not is_even(x)

# Call is_odd and is_even functions with different values
print(is_odd(17))
print(is_even(23))
