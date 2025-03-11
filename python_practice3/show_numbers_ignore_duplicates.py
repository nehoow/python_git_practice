#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers = set()
for i in range(10):
    user_input = int(input("Input numbers: "))
    numbers.add(user_input)

print (numbers)
