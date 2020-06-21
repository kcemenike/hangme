from set_difficulty import set_difficulty
from get_random import get_random
import numpy as np


def run_game():
    difficulty = set_difficulty()

    if difficulty:
        random_word = get_random(
            min_length=difficulty['min_word_length'],
            max_length=difficulty['max_word_length']
        )
        print(random_word)
        print(difficulty)

        number_of_tries = difficulty['number_of_tries']
        new_word = random_word
        guessed_letters = []
        while number_of_tries > 0:
            obfuscated_word = []
            letter = input("Please guess a letter in the hidden word\n")
            if (not letter) or (not letter.isalpha()) or len(letter) != 1:
                print("Wrong input, please try again")
                continue
            if letter in guessed_letters:
                print("You have already guessed this letter, please try again")
                continue
            else:
                guessed_letters.append(letter)
                print(f"You entered letter {letter.upper()}", end=" ")
                if letter in random_word:
                    print(
                        "\nYou have entered a correct letter\nPlease find the position below")
                    for letter in guessed_letters:
                        new_word = new_word.replace(letter, "")
                    is_wrong = False

                else:
                    print("which is not in the word :-(")
                    is_wrong = True

                # create a matrix to hold 1's for correct letters and 0 for wrong letters e.g. ['1', '0', '0']
                matrix = list(
                    np.array(
                        [
                            [1 if letter in item else 0 for item in random_word]
                            for letter in guessed_letters
                        ], dtype=int
                    ).sum(axis=0).astype(str)
                )

                # loop through matrix to change 0's to '*' and 1's to the guessed letter
                for index, item in enumerate(random_word):
                    if matrix[index] == '0':
                        obfuscated_word.append("*")
                    else:
                        obfuscated_word.append(item)
                print((''.join(obfuscated_word)).upper())

                if len(new_word) == 0:
                    print(
                        "You have successfully guessed all the letters.\nCongratulations!!!")
                    break

                if not is_wrong:
                    print(f"You have {number_of_tries} tries remaining")
                else:
                    print(
                        f"You have guessed the following letters so far\n{''.join(guessed_letters)}")

            # decrement counter based on value of is_wrong (True or False)
            number_of_tries -= is_wrong

        else:
            print(f"""
Sadly, you have run out of tries without guessing the complete word...
The word is {random_word.upper()}
GAME OVER!!!
""")
        try_again()
    else:
        print("System will now exit...")


def try_again():
    tryAgain = input(
        "Press 'y' to play again, or press any key to exit the game\n")
    if tryAgain == 'y':
        run_game()
    else:
        print("System will now exit")


run_game()
