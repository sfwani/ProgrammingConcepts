'''
Description: the program creates a while loop that allows us to get the factorial of a number
it takes input from the user first and converts it into an int
it then puts the number into a while loop that gives us the factorial of that number
program then prints out the factorial on screen
'''

number = int(input("Enter a non-negative integer:\n"))
while number < 0:
    number = int(input("Enter a nonnegative integer:"))

i = 1
f = 1

while i <= number:
    f = f * i
    i = i + 1
     
print(f'The factorial of {number} is {f:,}')

