#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuanDelaCruz

#ask the user their full name in incorrect casing
name = input("Enter your fullname in incorrect casing: ")
#capitalize everything and remove space
pascal_case_name = name.title().replace(' ','')
#print result
print(pascal_case_name)