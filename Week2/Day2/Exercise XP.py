#EX1
def display_message():
    print('I am learning python')

display_message()

#EX2
def favorite_book(title):
    print(f'My fav book is {title}')

favorite_book('Alice in Wonderland')

#EX3
def describe_city(name_of_city, country):
    print(f'{name_of_city} is in {country}')

describe_city('Beijing','China')

#EX4
import random
def compare_num(x):
    y = random.randint(1,100)
    if x != y:
        print(f'The numbers we chose are not the same {x},{y}')
    else:
        print(f'Success! we got the same num!{x}')

compare_num(7)

#EX5
def make_shirt(size,text):
    print(f'The size of the shirt is {size} and the text is {text}')

make_shirt('S','We love DS')

def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

make_shirt()
make_shirt("Medium")
make_shirt("Small", "Code is Life!")

#Ex6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    print(magician_names)

show_magicians()

def make_great():
    global magician_names 
    magician_names = list(map(lambda x: f"The Great {x}", magician_names)) 

make_great()
show_magicians()


#EX7
def get_random_temp():
    return int(random.randint(-10,40))

print(get_random_temp())

def main():
    x = get_random_temp()