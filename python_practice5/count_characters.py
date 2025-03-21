#Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.
#Example:
#Input: Juan Dela Cruz
#Output: 14

#ask the user for their full name
name = input("Enter your full name: ")
#count the characters using len()
char_count = len(name)
#print the result
print(char_count)