# INPUT.

input("Please enter a number:\n")
# Gets input while presenting a prompt to the user
# Can be assigned to a variable
# \n is an escape character used to print a new line
# Common escape characters are
# \n line feed
# \ ignore newline: used when your code spans multiple lines
# \t tab
# \\ backslash
# \' single quote

age = input("Please enter your age:\n")
print(type(age))
# input always returns a string
# You'll need to convert to any type you need

age = int(input("Please enter your age:\n"))
print(age)
print(type(age))
