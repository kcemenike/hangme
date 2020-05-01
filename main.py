# -*- coding: utf-8 -*-



# This is the hangman word game
import random


def print_scaffold(guesses, sth): # function that prints the hangman scaffold in a later version; just a sequence of prints for now.
		if (guesses == 0):
				print ("The beginning...")
				
		elif (guesses == 1):
				print ("First wrong guess")
		elif (guesses == 2):
				print ("Second wrong guess")
		elif (guesses == 3):
				print ("Third wrong guess")
		elif (guesses == 4):
				print ("Fourth wrong guess")
		elif (guesses == 5):
				print ("Fifth wrong guess")
				print ("\n")
				print ("The word was %s." %sth)
				print ("\n")
				print ("\n YOU LOSE! TRY AGAIN!")
				print ("\n Would you like to play again, type 1 for yes or 2 for no?")
				again = str(input("> "))
				again = again.lower()
				if again == "1":
				  hangMan()
				return

def selectWord():
	file = open('SAMPLES.txt')
	words = file.readlines() 
	myword = 'a'  #placeholder for random word to be selected from file.
	while len(myword) < 4: # makes sure word is at least 4 letters long
            myword = random.choice(words)  #randomly select word
            myword = str(myword).strip("''") #remove any single quotes from the words
            myword = str(myword).strip("\n") #remove any 'next line' from the words
            #myword = str(myword).strip("\r")
            myword = myword.lower() 
	return myword


def hangMan():
  guesses = 0					
  word = selectWord()				
  word_list = list(word)	
  blanks = "_"*len(word)	
  blanks_list = list(blanks) 
  new_blanks_list = list(blanks)
  guess_list = [] #list of guesses made by the player
  
  print ("Let's play hangman!\n")
  print_scaffold(guesses, word)
  print ("\n")
  print ("" + ' '.join(blanks_list))
  print ("\n")
  print ("Guess a letter.\n")
  
  while guesses < 5:    #Opportunity for five wrong attempts
  
  		guess = str(input("> "))
  		guess = guess.lower()
  		
  		if len(guess) > 1:
  				print ("Stop cheating! Enter one letter at time.")
  		elif guess == "":
  				print ("Don't you want to play? Enter one letter at a time.")
  		elif guess in guess_list:
  				print ("You already guessed that letter! Here is what you've guessed:")
  				print (' '.join(guess_list))
  		else:
  				guess_list.append(guess)
  				i = 0
  				while i < len(word):
  						if guess == word[i]:
  								new_blanks_list[i] = word_list[i]
  						i = i+1
  
  				if new_blanks_list == blanks_list:
  						print ("Your letter isn't here.")
  						guesses = guesses + 1
  						print_scaffold(guesses, word)
  						
  						if guesses < 6:
  								print ("Guess again.")
  								print (' '.join(blanks_list))
  						
  				elif word_list != blanks_list:
  						
  						blanks_list = new_blanks_list[:]
  						print (' '.join(blanks_list))
  						
  						if word_list == blanks_list:
  						  print ("\nYOU WIN! Here is your prize:\\://")
  						  print ("\n")
  						  print ("Would you like to play again?")
  						  print ("Type 1 for yes or 2 for no.")
  						  again = str(input("> "))
  						  if again == "1":
  						    hangMan()
  						  exit(0)
  						
  						else:
  								print ("Great guess! Guess another!")
												
hangMan()



	









