import random

word_list = ['apples', 'guavas', 'bananas', 'pears', 'blueberries']

word = random.choice(word_list)
# print(word)


    
def check_guess(guess):
    if len(guess) == 1 and guess.isalpha():
        return True
    else:
        return False

def ask_for_input():
    while True:
        guess = input('Enter a single letter: ')
        if check_guess(guess):
            if guess.lower() in word:
                print(f'Good guess {guess.lower()} is in the word {word}')
                break
            else:
                print(f'Sorry, {guess} is not in the word {word}. Try again.')
                break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
            continue

ask_for_input()