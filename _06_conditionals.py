# CONDITIONALS

names = ['A', 'B', 'C']
ages = [60, 13, 21]
population = dict(zip(names, ages))

# Can we extract over-18-year olds from the population?

# We can create a dictionary that is populated if the age is greater than 18
threshold_age = 18

over_18 = {}
for name in population:
    if population[name] >= threshold_age:
        over_18[name] = population[name]

print(over_18)

# There's also an option to use a list comprehension with condition
over18 = {name: population[name]
          for name in population if population[name] >= threshold_age}
