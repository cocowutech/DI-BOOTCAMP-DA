#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.


user_string = input('type a 10 char long string')
if len(user_string) < 10:
    print('string not long enough')
elif len(user_string) > 10:
    print('string too long')
else:
    print('perfect string')

#Then, print the first and last characters of the given text
print(user_string[0])
print(user_string[-1])


 #Using a for loop, construct the string character by character:
 # Print the first character, then the second, then the third, until the full string is printed. 

con_string = ''
for letter in user_string:
   con_string = con_string + letter
   print(con_string)

#shuffle
import random
user_list = list(user_string)
random.shuffle(user_list)
shuffled_string = ''.join(user_list)
print(str(shuffled_string))