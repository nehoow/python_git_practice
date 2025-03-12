#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
numbers = []
for i in range(10):
    user_input = int(input("Input a number: "))
    numbers.append(user_input)

# Find duplicates
duplicates = set()
seen = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)

# Display duplicates
if duplicates:
    print("Duplicate numbers:", *duplicates)
else:
    print("No duplicates found.")
