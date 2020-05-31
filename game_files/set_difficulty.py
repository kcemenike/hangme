'''This module is used to set the difficulty
The difficulty is a function of the randomly generated word length
easy = min_word_length=5, max_word_length=6, number_of_tries=5
normal = min_word_length=7, max_word_length=9 number_of_tries=7
hard = min_word_length=11, max_word_length=16, number_of_tries=8
impossible = min_word_length=12, max_word_length=16, number_of_tries=4
'''


def set_difficulty(selection=None, min_word_length=5, max_word_length=7, number_of_tries=5):
    while selection != 0:
        selection = input("""Please choose a difficulty level by typing the corresponding number.
            Enter 0 to exit
            1 - Easy
            2 - Normal
            3 - Hard
            4 - Impossible

            Enter 0 to exit
            """)
        try:
            selection = int(selection)
            while selection != 0:
                if selection == 1:
                    min_word_length = 5
                    max_word_length = 6
                    number_of_tries = 6
                elif selection == 2:
                    min_word_length = 7
                    max_word_length = 9
                    number_of_tries = 7
                elif selection == 3:
                    min_word_length = 10
                    max_word_length = 12
                    number_of_tries = 10
                elif selection == 4:
                    min_word_length = 11
                    max_word_length = 16
                    number_of_tries = 8
                else:
                    print("You have entered a wrong number")
                    break
                difficulty = {
                    "min_word_length": min_word_length,
                    "max_word_length": max_word_length,
                    "number_of_tries": number_of_tries
                }
                return difficulty
        except:
            print("You have entered a wrong value...")
