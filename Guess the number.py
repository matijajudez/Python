SECRET = 7
customer_name = input('What is your name? ')
print('Welcome to Casino', customer_name,'!')
print('For you we have a game called Guess the secret number. If you guess the secret number you get the reward. The number is less than 100 and you can only guess once!')

customer_guess = int(input('Type the number: '))

if SECRET == customer_guess:
    print('CONGRATULATION', customer_name, ', you guess the number corret. You get your reward of 1000$')
else:
    print('The number is wrong. But you can still win some others games!')

