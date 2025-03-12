#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
numbers = []
while True:
    try:
        user_input = int(input("Input a number: "))
        numbers.append(user_input)
    except ValueError:
        print("Invalid Input")
        numbers.sort(reverse=True)
        print("Numbers from highest to lowest:", numbers)
        break