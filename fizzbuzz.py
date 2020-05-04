print("Welcome to python FizzBuzz game. You must enter the number between 1-100.")

number = int(input("Enter the number: "))

for x in range(1, number + 1):

    if (x % 5 == 0) and (x % 3 == 0):
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)
