#Magic methods are special methods which have double underscores at the beginning and end of their names. 
#They are also known as dunders. 
#So far, the only one we have encountered is __init__, but there are several others. 
#They are used to create functionality that can't be represented as a normal method. 
#One common use of them is operator overloading. 
#This means defining operators for custom classes that allow operators such as + and * to be used on them.
#An example magic method is __add__ for +. 
# Define the Vector2D class
class Vector2D:
    def __init__(self, x, y):  # Initialize the Vector2D object with x and y coordinates
        self.x = x  # Assign the x coordinate to the instance variable 'x'
        self.y = y  # Assign the y coordinate to the instance variable 'y'

    def __add__(self, other):  # Define the addition operator method
        # Create a new Vector2D object by adding the corresponding x and y coordinates
        return Vector2D(self.x + other.x, self.y + other.y)

# Create two Vector2D instances
first = Vector2D(5, 7)
second = Vector2D(3, 9)

# Perform addition using the '+' operator, which invokes the '__add__' method
result = first + second

# Print the x and y coordinates of the resulting vector
print(result.x)
print(result.y)

#The __add__ method allows for the definition of a custom behavior for the + operator in our class.
#As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
#Once it's defined, we can add two objects of the class together.

print("*************************************************")
#More magic methods for common operators:
#__sub__ for -
#__mul__ for *
#__truediv__ for /
#__floordiv__ for //
#__mod__ for %
#__pow__ for **
#__and__ for &
#__xor__ for ^
#__or__ for |
#The expression x + y is translated into x.__add__(y). 
#However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called. 
#There are equivalent r methods for all magic methods just mentioned.
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        # Create a line of "=" characters with the same length as `other.cont`
        line = "=" * len(other.cont)
        # Concatenate the strings with the line of "=" in between
        return "\n".join([self.cont, line, other.cont])

# Create an instance of SpecialString with "spam" as its content
spam = SpecialString("spam")
# Create another instance of SpecialString with "Hello world!" as its content
hello = SpecialString("Hello world!")

# Call the __truediv__ method of the `spam` object, passing `hello` as the `other` parameter
# The __truediv__ method concatenates the strings with a line of "=" in between
# The result is printed to the console
print(spam / hello)

print("*"*40)
#Python also provides magic methods for comparisons.
#__lt__ for <
#__le__ for <=
#__eq__ for ==
#__ne__ for !=
#__gt__ for >
#__ge__ for >=
# If __ne__ is not implemented, it returns the opposite of __eq__. 
#There are no other relationships between the other operators.
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        # Iterate over the range of indices in `other.cont` and one additional index
        for index in range(len(other.cont) + 1):
            # Create a new string by inserting ">" between `other.cont[:index]` and `self.cont`
            result = other.cont[:index] + ">" + self.cont
            # Append the remaining portion of `other.cont` after the inserted ">"
            result += ">" + other.cont[index:]
            # Print the resulting string
            print(result)

# Create an instance of SpecialString with "spam" as its content
spam = SpecialString("spam")
# Create another instance of SpecialString with "eggs" as its content
eggs = SpecialString("eggs")

# Call the __gt__ method of the `spam` object, passing `eggs` as the `other` parameter
# The __gt__ method generates and prints strings with ">" characters inserted at different positions
spam > eggs

#There are several magic methods for making classes act like containers.
#__len__ for len()
#__getitem__ for indexing
#__setitem__ for assigning to indexed values
#__delitem__ for deleting indexed values
#__iter__ for iteration over objects (e.g., in for loops)
#__contains__ for in
#There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.


