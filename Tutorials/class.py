#Classes are created using the keyword class and an indented block, which contains class methods (which are functions). 
#Below is an example of a simple class and its objects.

class Cat:
  def __init__(self, color, legs):
    # The __init__ method is a special method called a constructor.
    # It is executed when a new instance of the Cat class is created.
    # It takes two parameters: `color` and `legs`.
    # The `self` parameter refers to the instance being created.
    
    # Assign the value of `color` parameter to the `color` attribute of the instance.
    self.color = color
    
    # Assign the value of `legs` parameter to the `legs` attribute of the instance.
    self.legs = legs

# Create three instances of the Cat class.
# The __init__ method will be called for each instance, initializing the attributes.

# Create an instance named felix with color "ginger" and legs 4.
felix = Cat("ginger", 4)

# Create an instance named rover with color "dog-colored" and legs 4.
rover = Cat("dog-colored", 4)

# Create an instance named stumpy with color "brown" and legs 3.
stumpy = Cat("brown", 3)

print(stumpy.color)

print("**********************Method in the Class****************************")
class Dog:
    def __init__(self, name, color):
        # The __init__ method is the constructor of the Dog class.
        # It is executed when a new instance of the class is created.
        # It takes two parameters: `name` and `color`.
        # The `self` parameter refers to the instance being created.
        
        # Assign the value of `name` parameter to the `name` attribute of the instance.
        self.name = name
        
        # Assign the value of `color` parameter to the `color` attribute of the instance.
        self.color = color

    def bark(self):
        # The `bark` method is a behavior (function) of the Dog class.
        # It takes no parameters (except `self`) and prints "Woof!".
        # The `self` parameter refers to the instance calling the method.
        
        print("Woof!")

# Create an instance of the Dog class named fido.
# The __init__ method will be called to initialize the attributes of the instance.

# Create an instance named fido with name "Fido" and color "brown".
fido = Dog("Fido", "brown")

# Access the `name` attribute of the fido instance and print its value.
print(fido.name)

# Call the `bark` method of the fido instance.
fido.bark()
