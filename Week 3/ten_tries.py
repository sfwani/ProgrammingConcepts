'''
Description: the program generates a random number and asks the user to guess it in 10 tries. 
It also hints if the number guessed was too high or too low compared to the random number.
If the user guesses it right, it congratulates the user and states the number of tries it took the user.
'''

import random

target = random.randint(1,100)
guesses = 0

while guesses < 10:
    guesses += 1
    user_input = int(input('Enter a number between 1 and 100 (inclusive): '))

    if user_input < 0: print('Really? Enter another guess between 1 to 100: ')
    elif user_input < target: print('Too low. Enter another guess: ')
    elif user_input > target: print('Too high. Enter another guess: ')
    else:
        print(f'You guessed it right!! You got it in {guesses} guesses! ')
        break

if guesses >= 10: print(f'Sorry, the number was {target}')