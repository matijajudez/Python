name = input("Hello, what's your name: ")
print("Welcome to python converter", name, ", here you enter numbers of KM and it will be convert to Miles.")

while True:

    kilometers = int(input("Enter the number of KM: "))
    miles = kilometers * 0.62137
    print(kilometers, "KM is", miles, "miles.")

    decision = input("Would you like to convert again(Yes or No): ")

    if decision.lower() != "Yes" and decision.lower() != "yes":
        break


print("Thank you for using our python converter. Goodbye", name)