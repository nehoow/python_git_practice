#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
user_input = int(input("Input a number:"))
difference = user_input
for i in range(9):
    user_input = int(input("Input a number:"))
    difference -= user_input
print("Result:", difference)
