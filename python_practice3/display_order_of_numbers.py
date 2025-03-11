#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
numbers = []

while True:
    try:
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)
    except ValueError:
        numbers.sort()  
        print("\nSorted numbers:", numbers)
        break  