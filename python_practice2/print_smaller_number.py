#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
first_user_input = int(input("First Number: "))
second_user_input = int(input("Second Number: "))
if first_user_input == second_user_input:
    print("They are equal.")
elif first_user_input < second_user_input:
    print("Smaller Number:", first_user_input)
else:
    print("Smaller Number:", second_user_input)