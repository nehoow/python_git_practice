#Prog03: Create a program that ask the user to input their fullname. Print the input in all capital letter.
#Example:
#Input: Juan Dela Cruz
#Output: JUAN DELA CRUZ

#Ask user to input their full name
full_name = input("Enter your full name: ")
#Using .upper to capitalize all letters.
capitalized_name = full_name.upper()
#print the capitalized string
print(capitalized_name)