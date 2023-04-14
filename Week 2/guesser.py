'''
Description: The program takes 4 integer values from a user and compares them against a randomly generated
value. If all the user values are above the randomly generated value, the program ends and no one is 
declared as the winner. However, if someone gets the exact number right, a message pops on the screen
saying someone has won.
At the end, the program reveals the random price that it had generated at the start and outputs the name 
of the person who wins that round. The user who wins the round has the number that was closest to the
random number without going above it.
'''

import random

price = random.randint(1000, 5000)
closest_bid = [0, 'placeholder_player']

player1_bid = int(input('Player 1, what is your bid? '))
if player1_bid <= price:
    closest_bid = [player1_bid, 'Player 1']
player2_bid = int(input('Player 2, what is your bid? '))
if player2_bid <= price:
    if player2_bid > closest_bid[0]:
        closest_bid = [player2_bid, 'Player 2']
player3_bid = int(input('Player 3, what is your bid? '))
if player3_bid <= price:
    if player3_bid > closest_bid[0]:
        closest_bid = [player3_bid, 'Player 3']
player4_bid = int(input('Player 4, what is your bid? '))
if player4_bid <= price:
    if player4_bid > closest_bid[0]:
        closest_bid = [player4_bid, 'Player 4']

if closest_bid[0] == 0:
    print('Buzz! Aww... everyone has overbid! ')
else:
    if closest_bid[0] == price:
        print('Ding Ding Ding! One player got it exactly right and gets $500!')
    print(f'Actual price is ${price}! {closest_bid[1]}, come on up! ')

