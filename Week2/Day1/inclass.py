def say_hello(name):
    print('hey '+name.capitalize() + ' you amazing!')

say_hello('coco')

def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' +last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

def format_name (first_name, last_name):
    return(first_name.title(),last_name.title())

first,last = format_name('coco','wu')
print(first)
print(last)

def calculation (a,b):
    return(a+b, a-b)

res = calculation(40,10)
print(res)


def greet_users(users):             # users should be a list
    for user in users:              # Because it's a list, we can loop through it
        print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

usernames = ["steve", "stan", "debbie"]
greet_users(usernames)

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
lesthanfour = filter(lambda x: len(x)<=4, people)
def greeting(name):
    return (f'Hi {name}')

print(list(map(greeting,lesthanfour)))
