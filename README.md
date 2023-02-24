# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 2
* The user is prompted to enter an input, this input is validated to be a single alphabetic character.

## Milestone 3
* Check if the guessed character is in the randomly selected word
Step 1. Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.

In the body of the loop, write the code required for the following steps.

Step 2: Ask the user to guess a letter and assign this to a variable called guess.

Step 3. Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.

Step 4. If the guess passes the checks, break out of the loop.

Step 5: If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."

## Milestone 4
### Class Hangman

Attributes:

* word
* word_guessed
* num_letters
* num_lives
* word_list
* list_of_guesses

Methods:

* check_guess
* ask_for_input

## Milestone 5

* play_game function creates instance of class Hangman
* Call play_game and pass in word_list as argument to start game