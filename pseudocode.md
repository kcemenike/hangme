# The game
How does HangMe work?

### Summary
- We ask the player to choose a word length (a.k.a. difficulty)
- A random word is generated (in this case, we'll be using English) with this length. In better terms, selected from an English dictionary of words. We can use words between 5 and 12 characters inclusive. Create a list from this word and another set (correct letter set) from the word
- We create a counter that counts down on the number of wrong attempts

- We start a loop that counts down as long as there are unguessed letters in the random word
    - We ask the player for input (input must be a single letter)
        - If the letter has been guessed before
            - Tell the player that letter has already been guessed
        - If the letter is in the word
            - Tell the player that he is correct
            - Remove the letter from the correct letter set
            - Tell the player the position(s) of the letter in the word
        - Else
            - Decrement counter
            - Add the guessed letter to the wrong letter set
    - If the word is solved
        - Success!!!
    - Else
        - Game over!
        - Give the player the option to try again