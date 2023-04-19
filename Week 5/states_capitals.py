'''
Description:
The program requires the user to guess the capital of a given state and keeps a record of the user's correct and incorrect answers. Additionally, the program will terminate when the user presses the 'q' key, which serves as the sentinel condition.
'''
import random

capitals = {
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City"
}
answer, correct, incorrect = '', 0, 0

while answer != 'q':
    state = random.choice(list(capitals))

    answer = input(f'What is the capital of {state}? (or press "q" to quit): ')
    if answer == capitals[state]:
        correct += 1
        print('That is correct.')
    elif answer == 'q':
        print('')
    else:
        incorrect += 1
        print('That is incorrect.')

print(f'You had {correct} correct response(s) and {incorrect} incorrect response(s).')