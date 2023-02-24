import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        letter = guess.lower()
        if letter in self.word:
            print(f'Good guess! {letter} is in the word.')
            
            for i, v in enumerate(self.word):
                if v == letter:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word.\n You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ')
            if len(guess) != 1 or not guess.isalpha():
                print(f'Invalid letter. Please, enter a single alphabetical characater.')
            elif guess in self.list_of_guesses:
                print(f'You already tried that letter!')
            else:
                self.check_guess(guess)
                print(self.word_guessed)
            self.list_of_guesses.append(guess)
            break

game_one = Hangman(['apple', 'cherry'])
game_one.ask_for_input()