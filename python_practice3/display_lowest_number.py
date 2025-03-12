#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
lesser = None  

while True:
    try:
        user_input = int(input("Input a number: "))

        if lesser is None or user_input < lesser:
            lesser = user_input

        print("Lowest so far:", lesser)

    except ValueError:
        print("\nFinal lowest number:", lesser)
        break 
