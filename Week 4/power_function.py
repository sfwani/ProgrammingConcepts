'''
Description:
This program calculates the power of a given base raised to a whole number exponent. It prompts the user to input the base and exponent and checks if the exponent is within the valid range (2 to 50). If the input is invalid, the program prompts the user to re-enter the exponent. The program then uses a recursive function to calculate the result and prints the output.
'''

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)

def main():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter a whole number between 2 and 50: "))
    while exponent < 2 or exponent > 50:
        exponent = int(input("Invalid. Please enter a whole number between 2 and 50: "))
    result = power(base, exponent)
    print("{} raised to the power of {} is {}".format(base, exponent, result))

if __name__ == '__main__':
    main()

