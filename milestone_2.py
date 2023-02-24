import random
#import re

word_list = ['apples', 'guavas', 'bananas', 'pears', 'blueberries']
#print(word_list)

word = random.choice(word_list)
print(word)

while True:
    guess = input('Enter a single letter: ')
    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
        break
    else:
        print('Oops! That is not a valid input.')
        continue