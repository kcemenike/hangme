# MODULES.
# In Python, you can import modules to do specialised functions
# The math module, for example, is used for mathematical computation
# You can also import your own .py files as modules

# To get the square root of a number we need to import math
# let us also import our own file as a module
import math
import _06_conditionals

number = 625
square_root = math.sqrt(number)
print(square_root)

# You notice that importing a module runs the module and all its
# contents to make the variables in the module available
# importing _06_conditionals automatically makes the dictionary available

# We can now get the variables in the _06_conditionals module
# e.g. the threshold_age
print(_06_conditionals.threshold_age)

print(dir(_06_conditionals))  # Allows us to get all objects in the module
