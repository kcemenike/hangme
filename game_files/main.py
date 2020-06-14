from set_difficulty import set_difficulty
from get_random import get_random

difficulty = set_difficulty()
WORDLIST = 'words_alpha.txt'

if difficulty:
    random_word = get_random(difficulty['min_word_length'], difficulty['max_word_length'], WORDLIST)
    print(random_word)
    number_of_tries = difficulty['number_of_tries']
    guessed_letters = []
    new_word = random_word
    while number_of_tries > 0:
        letter = input("Please guess a letter in the hidden word\n")
        # check if letter is a character // length of letter = 1
        if (len(letter) != 1) or (not letter.isalpha()) or (not letter):
            print("Wrong input, please try again")
            continue # breaks out the current iteration of the loop
        if letter in guessed_letters:
            print("You have already guessed this letter, please try again")
            print(guessed_letters)
            continue
        else:
            guessed_letters.append(letter)

        # if letter in word
        if letter in random_word:
            print("You have guessed a correct letter. Excellent!")
            new_word = new_word.replace(letter, '')
            print(random_word, new_word)
        else:
            number_of_tries -= 1
            print("Wrong letter, please try again")

        # keep track of the length of the word
        if len(new_word) == 0:
            print("You have successfully guessed all the letters.\nCongratulations!!!")
            break
    #     print(number_of_tries)
    else:
        print(f"""Sadly, you have run out of tries without guessing the word....
        The word is {random_word.upper()}
        GAME OVER!!!
        """)    
else:
    print("Code will now exit")
    
    
