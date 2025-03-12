#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
sum = 0
for i in range(10):
    user_input = int(input("Input a number: "))
    sum += user_input
print("Sum of all numbers:", sum)