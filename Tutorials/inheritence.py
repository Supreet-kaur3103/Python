#Inheritance provides a way to share functionality between classes. 
#Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name). 
#This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality. 
#To inherit a class from another class, put the superclass name in parentheses after the class name.
class Animal:
    def __init__(self, name, color):
        # The __init__ method is the constructor of the Animal class.
        # It is executed when a new instance of the class is created.
        # It takes two parameters: `name` and `color`.
        # The `self` parameter refers to the instance being created.
        
        # Assign the value of `name` parameter to the `name` attribute of the instance.
        self.name = name
        
        # Assign the value of `color` parameter to the `color` attribute of the instance.
        self.color = color

class Cat(Animal):
    def purr(self):
        # The `purr` method is a behavior (function) specific to the Cat class.
        # It takes no parameters (except `self`) and prints "Purr...".
        # The `self` parameter refers to the instance calling the method.
        
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        # The `bark` method is a behavior (function) specific to the Dog class.
        # It takes no parameters (except `self`) and prints "Woof!".
        # The `self` parameter refers to the instance calling the method.
        
        print("Woof!")

# Create an instance of the Dog class named fido.
# The __init__ method of Animal class is called to initialize the attributes of the instance.

# Create an instance named fido with name "Fido" and color "brown".
fido = Dog("Fido", "brown")

# Access the `color` attribute of the fido instance and print its value.
print(fido.color)

# Call the `bark` method of the fido instance.
fido.bark()


#A class that inherits from another class is called a subclass.
#A class that is inherited from is called a superclass.
#If a class inherits from another with the same attributes or methods, it overrides them. 

print("*********************************************************************")
#The function super is a useful inheritance-related function that refers to the parent class. It can be used to find the method with a certain name in an object's superclass.
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
            
B().spam()

print("**********************************************************")
# Define the Shape class
class Shape: 
    def __init__(self, w, h):  # Initialize the Shape object with width and height
        self.width = w  # Assign the width to the instance variable 'width'
        self.height = h  # Assign the height to the instance variable 'height'

    def area(self):  # Define the area method
        print(self.width * self.height)  # Print the area of the shape by multiplying width and height

# Define the Rectangle class as a subclass of Shape
class Rectangle(Shape):
    def perimeter(self):  # Define the perimeter method specific to Rectangle
        print(2 * (self.width + self.height))  # Print the perimeter of the rectangle

# Get the input for width and height from the user
w = int(input())  # Prompt the user to enter the width and convert it to an integer
h = int(input())  # Prompt the user to enter the height and convert it to an integer

# Create an instance of Rectangle with the given width and height
r = Rectangle(w, h)

# Call the area method of Rectangle
r.area()

# Call the perimeter method of Rectangle
r.perimeter()
