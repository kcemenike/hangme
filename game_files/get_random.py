'''
Get random word from a long list of words
'''

# Import modules

# Get random word from file
# import random
# import re
# WORDLIST = 'dictionary.csv'


# def get_random(difficulty=1, min_length=5, max_length=7, wordlist=WORDLIST):
#     '''Get a random word of a minimum length from a wordlist file'''
#     words = []
#     with open('dictionary.csv') as file:
#         for dict_word in file:
#             # get word from file
#             word = re.findall(r"\w+", dict_word)[0].lower()
#             # print(min_length, len(word), max_length)
#             if min_length <= len(word) <= max_length:
#                 # change to lowercase and append to words list
#                 words.append(word)
#         # print(len(words))
#     return random.choice(words)  # return random choice from list

import random


def get_random(min_length, max_length, wordlist='words_alpha.txt'):

    WORDLIST = wordlist
    words = []
    with open(WORDLIST, 'r') as file:
        for word in file:
            word = word.strip('\n').lower()
            if min_length <= len(word) <= max_length:
                words.append(word)
    return random.choice(words)
