#Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class. 
#They are marked with the staticmethod decorator.
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        # Check if the topping is "pineapple"
        if topping == "pineapple":
            # If the topping is "pineapple", raise a ValueError with the message "No pineapples!"
            raise ValueError("No pineapples!")
        else:
            # If the topping is not "pineapple", return True
            return True

# List of ingredients for the pizza
ingredients = ["cheese", "onions", "spam"]

# Check if all the toppings in ingredients pass the topping validation using the static method validate_topping
if all(Pizza.validate_topping(i) for i in ingredients):
    # Create an instance of Pizza if all the toppings are valid
    pizza = Pizza(ingredients)

print("*"*40)
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @staticmethod
    def area(w,h):
        return w*h

w = 5
h = 7

print (Shape.area(w,h))       