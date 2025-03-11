#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
seen = set()

while True:
    try:
        user_input = int(input("Input a number: "))  
  

        if user_input in seen:
            print("Duplicate")
        else:
            print("Unique")
            seen.add(user_input)  
    except ValueError:
        print("Invalid input. Exiting...")
        break  
