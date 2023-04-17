'''
Description:
The program prompts the user to ask a yes-or-no question and generates a random response from a list of 20 possible answers. The program includes two functions:
1. main function - which prompts the user for a question, generates a random number, and calls the function to print the response.
2. print_response function - which prints the response using a local list of standard responses. 
The program also includes a while loop to repeat the process if the user wants to ask another question. 
The loop continues as long as the user inputs a response other than 'no'.
'''

import random

def print_response(num):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 
                 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 
                 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 
                 "Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
    print(responses[num])

def main():
    while True:
        question = input('What is your question? ')
        response_num = random.randint(0, 19)
        print_response(response_num)
        repeat = input('Would you like to ask another question? ')
        if repeat.lower() == 'no':
            break

if __name__ == '__main__':
    main()
