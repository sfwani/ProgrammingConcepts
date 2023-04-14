'''
Description: The program asks the user for their friends' eating preferences that could help the program decide
on what the best place to eat would be for him and his friends. It is done by checking against the food options
that multiple restaurants in the area have and matching them against the preferences of everyone.
'''

restaurants = ['True Food Kitchen', 'Gourmet Pizza Company', "Bella's Italian Restaurant", "Fleming's Prime Steakhouse"]

is_vegetarian = (input('Is anyone in your party a vegetarian? ')).lower()
is_vegan = (input('Is anyone in your party a vegan? ')).lower()
is_gluten_free = (input('Is anyone in your party gluten free? ')).lower()

if is_vegan == 'yes':
    print('Here are your restaurant choices:')
    print(restaurants[0])
elif is_gluten_free == 'yes':
    print('Here are your restaurant choices:')
    print(restaurants[0] + '\n' + restaurants[1])
elif is_vegetarian == 'yes':
    print('Here are your restaurant choices:')
    print(restaurants[0] + '\n' + restaurants[1] + '\n' + restaurants[2])
else:
    print('Here are your restaurant choices:')
    print(restaurants[0] + '\n' + restaurants[1] + '\n' + restaurants[2] + '\n' + restaurants[3])