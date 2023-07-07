#Properties provide a way of customizing access to instance attributes. 
#They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead. 
#One common use of a property is to make an attribute read-only.
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    # This property method is used to determine whether pineapple is allowed as a topping on the pizza.
    # In this case, it always returns False, indicating that pineapple is not allowed.
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)  # Prints: False

pizza.pineapple_allowed = True  # This line will raise an AttributeError since the property is read-only.

# Explanation:
# The `@property` decorator is used to define a getter method that allows accessing the property like an attribute,
# without using parentheses. In this case, the property `pineapple_allowed` is read-only since there is no setter method defined.

# The `Pizza` class represents a pizza object. It is initialized with a list of toppings passed as an argument to the constructor.
# The `toppings` attribute stores the list of toppings.

# The `pineapple_allowed` property provides a way to check if pineapple is allowed as a topping on the pizza.
# However, since it only has a getter method and no setter, the property is read-only, and attempting to assign a new value to it will raise an AttributeError.

# In the example, a `Pizza` object named `pizza` is created with toppings ["cheese", "tomato"].
# The `pineapple_allowed` property is accessed using `pizza.pineapple_allowed`, which returns False and is then printed.

# Finally, when trying to assign `True` to `pizza.pineapple_allowed`, an AttributeError is raised, indicating that the property is read-only and cannot be modified.

print("*"*40)
#Properties can also be set by defining setter/getter functions.
#The setter function sets the corresponding property's value.
#The getter gets the value.
#To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
#The same applies to defining getter functions.
class Pizza:
  def __init__(self, toppings):
    # The constructor method of the Pizza class.
    # It initializes the instance with a list of toppings passed as an argument.
    self.toppings = toppings

    # Private variable to store the state of whether pineapple is allowed as a topping.
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    # A property getter method to retrieve the value of `_pineapple_allowed`.
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    # A property setter method to set the value of `_pineapple_allowed`.
    # It performs additional checks and requires a password for allowing pineapple.

    if value:
      # If the value being set is True (allowing pineapple), proceed with password validation.

      password = input("Enter the password: ")  # Prompting the user to enter a password.

      if password == "Sw0rdf1sh!":
        # If the entered password matches the expected password, allow pineapple by updating `_pineapple_allowed`.
        self._pineapple_allowed = value
      else:
        # If the entered password is incorrect, raise a ValueError indicating an intrusion attempt.
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])  # Creating a Pizza object with toppings ["cheese", "tomato"].

print(pizza.pineapple_allowed)  # Printing the current state of pineapple_allowed (False).

pizza.pineapple_allowed = True  # Setting pineapple_allowed to True.

print(pizza.pineapple_allowed)  # Printing the updated state of pineapple_allowed (True).

# Explanation:
# The `Pizza` class represents a pizza object. It has a constructor method `__init__` that initializes the instance with a list of toppings.

# The private variable `_pineapple_allowed` is initialized as False when a `Pizza` object is created.

# The `pineapple_allowed` property provides a way to get and set the value of `_pineapple_allowed`.
# The getter method is decorated with `@property`, allowing it to be accessed like an attribute without parentheses.
# The setter method is decorated with `@pineapple_allowed.setter`, enabling assignment to the property.

# In the setter method, if the value being set is True, the user is prompted to enter a password.
# If the entered password matches the expected password ("Sw0rdf1sh!"), the `_pineapple_allowed` variable is updated.
# Otherwise, a ValueError is raised to indicate an intrusion attempt.

# In the example, a `Pizza` object named `pizza` is created with toppings ["cheese", "tomato"].
# The current state of `pineapple_allowed` (False) is printed.

# The property `pineapple_allowed` is then set to True by assigning `True` to `pizza.pineapple_allowed`.
# This triggers the setter method, which prompts the user to enter a password.
# If the correct password is entered, `_pineapple_allowed` is updated to True.

# Finally, the updated state of `pineapple_allowed` (True) is printed.

print("*"*40)
class Player:
    def __init__(self, name, lives):
        # The constructor method of the Player class.
        # It initializes the player with a name and a number of lives.
        self.name = name
        self._lives = lives

    def hit(self):
        # A method that represents the player being hit, reducing their lives by 1.
        self._lives -= 1
    
    @property
    def isAlive(self):
        # A property getter method to check if the player is still alive.
        # It returns True if the player's remaining lives are greater than 0, otherwise returns False.
        return self._lives > 0

# Creating a Player object with a name provided by the user and an initial number of lives.
p = Player("Cyberpunk77", int(input()))

i = 1
while True:
    p.hit()  # Simulating the player being hit.
    print("Hit # " + str(i))  # Printing the current hit number.
    i += 1

    if not p.isAlive:
        # If the player is no longer alive (remaining lives <= 0), print "Game Over" and break out of the loop.
        print("Game Over")
        break

# Explanation:
# The `Player` class represents a player with a name and a number of lives.
# The constructor method `__init__` initializes the instance with the provided name and lives.

# The `hit` method reduces the player's lives by 1 each time it is called.

# The `isAlive` property provides a way to check if the player is still alive.
# The getter method is decorated with `@property` to allow accessing it like an attribute.

# In the code, a `Player` object named `p` is created with a name provided by the user and an initial number of lives.
# The variable `i` is used to keep track of the hit number.

# In the while loop, the player is simulated being hit by calling `p.hit()`.
# The current hit number is printed, and `i` is incremented.

# After each hit, the condition `if not p.isAlive` is checked to see if the player is still alive.
# If the player is no longer alive (remaining lives <= 0), "Game Over" is printed, and the loop is broken with `break`.
