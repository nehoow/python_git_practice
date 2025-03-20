#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuaN deLA cRuz

#ask user to input their fullname with incorrect casing
full_name = input("Enter your fullname with incorrect casing: ")
#reverse the casing by using .swapcase()
swapped_case_name = full_name.swapcase()
#print sa swapped cased name
print(swapped_case_name)