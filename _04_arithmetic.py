# BASIC ARITHMETIC
# Objects can be added, subtracted, multiplied, etc

price = 20.0
quantity = 5

total = price * quantity
print(total)

names = ['A', 'B', 'C']
ages = [60, 13, 21]
population = dict([
    ('A', 60),
    ('B', 13),
    ('C', 21)
])  # looks stressful

# Let's introduce a function called zip
population = dict(zip(names, ages))
# Learn more about zip from the Python documentation

# If we want to multiply each age by 365 to get the number of days
# If we try ages * 365, it will return an error

# This is where we need to find a way to loop through the ages variable in the next lesson
