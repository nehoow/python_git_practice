#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
sum = 0
count = 0
while True:
    try:
        user_input = float(input("Input a number: "))
        sum += user_input
        count += 1

    except ValueError:
        print ("Invalid Input.")
        print ("Average:",sum / count)
        break