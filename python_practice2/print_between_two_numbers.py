#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
first_user_input = int(input("First Number: "))
second_user_input = int(input("Second Number: "))
if first_user_input == second_user_input:
    print("They are equal.")
elif first_user_input > second_user_input:
    for i in range(second_user_input + 1, first_user_input):
        print (i)
else:
     for i in range(first_user_input + 1, second_user_input):
        print (i)