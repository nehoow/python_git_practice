#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#Example:
#Input: We will weather the weather whatever the weather whether we like it or not
#Output: 14

#Ask the user to input a complete statement
statement = input("Input a whole statement: ")
#split the string to different words using .split
word = statement.split()
#we will count the number of words inside the list of the split
word_count = len(word)
#print count
print(word_count)