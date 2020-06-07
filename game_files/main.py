from set_difficulty import set_difficulty
from get_random import get_random

difficulty = set_difficulty()
WORDLIST = 'words_alpha.txt'

if difficulty:
    random_word = get_random(difficulty['min_word_length'], difficulty['max_word_length'], WORDLIST)
    print(random_word)
else:
    print("Code will now exit")