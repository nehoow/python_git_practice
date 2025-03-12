#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
numbers = []
max_count = 0
most_repeating = None
while True:
    try:
        user_input = int(input("Input a number: "))
        numbers.append(user_input)

        for num in set(numbers):
            count = numbers.count(num)
            if count > max_count:
                max_count = count
                most_repeating = num
    except ValueError:
        print("Invalid Input.")
        print("Most repeated number:", most_repeating)
        break