'''
Description:
This code defines a calculator function that takes in an operation and two values (x and y) as arguments. Depending on the operation, the function returns a lambda function that performs the corresponding mathematical operation on x and y. The main part of the code prompts the user to input an operation and two values, and then calls the calculator function with those values. It then calls the resulting lambda function and stores the result in a variable called "result". Finally, the program prints out the original values, the operation, and the result of the calculation.
'''

def calculator(operation, x, y):
    if operation == '+' or operation == 'add':
        return lambda: x + y
    elif operation == '-' or operation == 'subtract':
        return lambda: x - y
    elif operation == '*' or operation == 'multiply':
        return lambda: x * y
    elif operation == '/' or operation == 'divide':
        if y == 0:
            return lambda: 'Division by zero is undefined'
        else:
            return lambda: x / y
    elif operation == '//' or operation == 'integer divide':
        if y == 0:
            return lambda: 'Division by zero is undefined'
        else:
            return lambda: x // y
    elif operation == '%' or operation == 'modulus':
        if y == 0:
            return lambda: 'Modulus by zero is undefined'
        else:
            return lambda: x % y
    elif operation == '**' or operation == 'exponent':
        return lambda: x ** y
    else:
        return lambda: f'Invalid operation {operation}'

operation = input('Enter the operation as a symbol (e.g. + for addition): ')
x, y = map(float, input('Enter two values, separated by a space: ').split())

result = calculator(operation, x, y)()

print(f'{x} {operation} {y} = {result}')
