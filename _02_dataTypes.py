# Objects and Data Types
# How do we differentiate between different things?

# A man is different from a woman for example, based on specific features
# Rice is different from spaghetti as well
# They are all objects, but some are rice "objects", some are spaghetti "objects", etc

# In Python, everything is an object
# Buitlin datatypes
# String e.g. '200'
# Integer e.g. 200
# List e.g. [2, 0, 0]
# Set e.g. (2, 0) a tuple/list without duplicates
# Float e.g. 200.0
# Boolean e.g. True
# Tuple e.g. (2, 0, 0)
# Dictionary e.g. {'Kelechi': 39, 'John': 35}

# Types can also be created using classes (advanced stuff, not for this beginner session)

# Mutability
# Mutability is the 'changeability' of individual items of an object
# e.g. changing 200 to 201 requires that it is entirely changed, and not a single 0 to 1
# Immutable objects: Integer, float, string, tuple, boolean
# Mutable objects: Collections (list, dicationary, sets)

# How do I know the datatype of an object? Use the type function
print(type(200))

print(type(200.0))

print(type('200'))

print(type(True))

print(type([2, 0, 0]))

print(type((2, 0, 0)))

print(type((2, 0)))

print(type({'number': 200}))

# ----------- QUIZ ------------- #
# You notice that (2, 0, 0) and (2, 0) are perceived as tuples.
# Can you figure out how to create a set object?

# TYPE CONVERSIONS
# To convert from one type to another (or to create an empty object), use the following functions
# Integer - int
# String - str
# Float - float
# Dictionary - dict
# Set - set
# Tuple - tuple
# Boolean - bool
# List - list

print(type(int(200.0)))  # converts the float 200.0 to an integer

# Try out other type conversions
