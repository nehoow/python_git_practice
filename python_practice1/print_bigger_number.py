#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
first_user_input = int(input("First Number: "))
second_user_input = int(input("Second Number: "))
if first_user_input == second_user_input:
    print("They are equal.")
if first_user_input > second_user_input:
    print("Bigger Number", first_user_input)
else:
    print("Bigger Number", second_user_input)