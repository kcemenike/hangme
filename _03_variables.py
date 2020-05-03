# Variables
# How can we store values?

# Think of a variable as an empty box. A box has:
# Size / Capacity
# What can be saved in it. If it's for noodles, it's a noodle box. Let's call it type

# So there are:
# string variables: variables that can hold strings
# integer variables, etc
# Variables naming rules
# Must start with a letter or underscore, and must contain alphanumeric characters
# Variables are case senstive

# Python tries to automatically define the type of a variable

age = 20  # this is an integer variable
print(type(age))

# Variables can be reassigned to another object
age = 20.0  # this is a float variable
print(type(age))

ages = [20, 10.0]  # this is a list variable
print(type(ages))
