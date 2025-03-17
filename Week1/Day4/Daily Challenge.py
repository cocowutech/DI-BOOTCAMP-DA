#1Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.
# Step 1: Get user input
number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

# Step 2: Generate the multiples using a list comprehension
multiples_list = [number * i for i in range(1, length + 1)]

# Step 3: Print the final list
print("Multiples:", multiples_list)

#2.
#Write a program that asks a string to the user, 
#and display a new string with any duplicate consecutive letters removed.

user_word = input('please enter a word and make duplicates of the letter during the word')
new_word = ''
for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i-1]:
        new_word = new_word + user_word[i]

print('cleaned:',new_word)