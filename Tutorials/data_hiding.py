#Weakly private methods and attributes have a single underscore at the beginning.
#This signals that they are private, and shouldn't be used by external code. However, it is mostly only a convention, and does not stop external code from accessing them.
class Queue:
    def __init__(self, contents):
        # Initialize the Queue with the provided contents as a list
        self._hiddenlist = list(contents)

    def push(self, value):
        # Insert the value at the beginning of the list using the insert() method
        self._hiddenlist.insert(0, value)

    def pop(self):
        # Remove and return the last element of the list using the pop() method with -1 as the index
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        # Return a string representation of the Queue object
        return "Queue({})".format(self._hiddenlist)

# Create an instance of Queue with [1, 2, 3] as its initial contents
queue = Queue([1, 2, 3])

# Print the string representation of the queue object
print(queue)
# Output: Queue([1, 2, 3])

# Add a new element, 0, to the queue using the push() method
queue.push(0)
# Print the updated string representation of the queue object
print(queue)
# Output: Queue([0, 1, 2, 3])

# Remove and return the last element from the queue using the pop() method
popped_value = queue.pop()
# Print the popped value
print(popped_value)
# Output: 3

# Print the string representation of the queue object after popping an element
print(queue)
# Output: Queue([0, 1, 2])

# Access the underlying hidden list directly
print(queue._hiddenlist)
# Output: [0, 1, 2]

print("*"*40)
#Strongly private methods and attributes have a double underscore at the beginning of their names. This causes their names to be mangled, which means that they can't be accessed from outside the class. 
#The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses that have methods or attributes with the same names.
#Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
class Spam:
    # Private class variable
    __egg = 7

    def print_egg(self):
        # Print the value of the private class variable
        print(self.__egg)

# Create an instance of the Spam class
s = Spam()

# Call the print_egg() method, which prints the value of __egg
s.print_egg()
# Output: 7

# Access the private class variable using the name mangling syntax
print(s._Spam__egg)
# Output: 7

# Trying to access the private class variable directly using __egg raises an AttributeError
# Uncommenting the line below will result in an AttributeError
# print(s.__egg)
# Output: AttributeError: 'Spam' object has no attribute '__egg'

