#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
numbers = []
for i in range(10):
    user_input = int(input("Input numbers: "))
    numbers.append(user_input)

for num in numbers:
    if numbers.count(num) == 1:
        print(num)