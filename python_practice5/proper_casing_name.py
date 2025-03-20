#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: Juan Dela Cruz

#ask the user to input their fullanme in incorrect casing
full_name = input("enter your fullname with incorrect casing: ")
#Use .title() to fix and put proper casing to the name
proper_casing_name = full_name.title()
#print the proper cased name
print(proper_casing_name)