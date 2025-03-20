#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Example:
#Input: 143
#Output: 000143
#ask user input for 0-1000
number = input("Input a number 0-1000: ")
#add zeroes by using zfill
sixdigit_number = number.zfill(6)
#print the result
print(sixdigit_number)