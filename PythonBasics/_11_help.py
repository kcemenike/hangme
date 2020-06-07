# CONFUSED?

# Not to worry, you can use the help function to learn anything

help(print)  # returns help on how to use the print function
help(str)   # returns help on how to use the string object

age = 20
help(age)  # return help on how to use the age object too!
# Since age is an integer, help shows how to us the integer object

# If the help function has too much information...
# To show all objects (i.e. methods and attributes) of an object, use the dir function
dir(age)
# You may (for now) ignore the __dunder__ variables (variables with double underscore)
age.imag  # returns the imaginary part of an integer (or 0 if it's not complex)
age.real  # returns the real part of an integer, and so on
