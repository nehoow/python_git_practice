#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
highest_number = None
while True:
    try:
        user_input = int(input("Input a number: "))
        if highest_number is None or user_input > highest_number:
            highest_number = user_input
    except ValueError:
        print ("Highest Number:", highest_number)
        break