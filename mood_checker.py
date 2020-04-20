print('Hello user!')
mood = input('In what mood are you today? ')

if mood == 'happy':
    print('It is great to see you happy!')
elif mood == 'nervous':
    print('Take a deep breathe 3 times.')
elif mood == 'sad':
    print('Today is a great day, so there is no place for being sad!')
elif mood == 'exited':
    print('Great, the day is yours, take it!')
elif mood == 'relaxed':
    print('It is good to be relaxed in this day, enjoy it!')
else:
    print("I don't recognize this mood.")
