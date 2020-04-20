print('Welcome to Python calculator!')

first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

operation = input('Select one operation. You can choose betwen +, -, /, * : ')

if operation == '+':
    print(first_number, '-', second_number, '+', first_number + second_number)
elif operation == '-':
    print(first_number, '-', second_number, '=', first_number - second_number)
elif operation == '/':
    print(first_number, '/', second_number, '=', first_number / second_number)
elif operation == '*':
    print(first_number, '*', second_number, '=', first_number * second_number)
else:
    print("I don't recognize this operation!")

