# LOOPS

names = ['A', 'B', 'C']
ages = [60, 13, 21]
population = dict(zip(names, ages))


# How can we multiply each age by 365 to get the number of days

for age in ages:
    print(age * 365)
    # allows me to print age but doesn't change the value of ages

# We can create a list variable called new_ages
# And then for each iteration, append the result to the new_ages
new_ages = []
for age in ages:
    new_ages.append(age*365)

print(new_ages)  # [21900, 4745, 7665]

# We can now create a new population from the new_ages with dict(zip(names, new_ages))

# Or we can as well create a new population directly from the population variable
new_population = {}  # initialise an empty dictionary
for name in population:
    new_population[name] = population[name] * 365

print(new_population)  # {'A': 21900, 'B': 4745, 'C': 7665}

# Or we can use a list (or dictionary comprehension) to create our new list (or dictionary)
new_ages = [age * 365 for age in ages]  # [21900, 4745, 7665]
new_population = {population[name] * 365 for name in population}
# {'A': 21900, 'B': 4745, 'C': 7665}
