#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
count = 0
for i in range(10):
    user_input = int(input("Input a number: "))
    if user_input % 2 == 0:
        count += 1
print ("Even numbers:", count)