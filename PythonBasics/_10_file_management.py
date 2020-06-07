# FILE MANAGEMENT

# How can I read the contents of a file into a variable?
# How can I write a variable to a file

# READING FILES
import os
from random import randint, sample
with open('words_alpha.txt') as file:
    words = file.read().split()

test = sample(words, 10)  # Get a sample of 10 words

os.remove('sample.txt')
with open('sample.txt', 'a') as file:
    for item in test:
        file.write(item+"\n")
