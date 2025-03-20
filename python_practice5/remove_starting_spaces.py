#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Example:
#Input:         Juan Dela Cruz
#Output: Juan Dela Cruz
full_name = input("Input your full name with several spaces in the beginning:")
removed_spaces_name = full_name.lstrip()
print(removed_spaces_name)