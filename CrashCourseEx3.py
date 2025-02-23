#1. Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).

list ={
    'name':'Elie', 
    'job':'Instructor'
}

print(list)

#2
name = ["CA", "NJ", "RI"]
full_name = ["California", "New Jersey", "Rhode Island"]
my_dict = dict(zip(name,full_name))
print(my_dict)

#3
vowel = ['a','e','i','o','u']
vowel_dict = {vow: 0 for vow in vowel}
print(dict)

#4
dict_key = range(1,27)
uppercase_letters = [chr(i) for i in range(65,91)]
letter_pair = dict(zip(dict_key,uppercase_letters))
print(letter_pair)

#5
string = 'awesome sauce'
vowels = 'aeiou'
vowel_dict = {vowel:string.count(vowel) for vowel in vowels }
print(vowel_dict)