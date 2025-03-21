#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Example:
#Input: jUAn DEla CrUZ
#Output: juan_dela_cruz

#ask the user in incorrect casing
name = input("Enter your fullname in incorrect casing: ")
#lower case everything with lower and replace all space to _
snake_case_name = name.lower().replace(' ','_')
#print the result
print(snake_case_name)