#EX1
my_fav_numbers = {1,2,3,4}
my_fav_numbers.add(5)
my_fav_numbers.add(6)
print(my_fav_numbers)
my_fav_numbers.remove(6)
print(my_fav_numbers)

friend_fav_numbers = {4,5,6,7,8}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Ex2
#Instructions
#Given a tuple which value is integers, is it possible to add more integers to the tuple?
tuple = (3,4,5)
#it's not mutable 

#ex3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
print(basket)
basket.insert(0,'Apples')
print(basket)
print(basket.count('Apples'))
basket.clear()
print(basket)

#ex4
mixed_numbers = [1.5 + (i * 0.5) for i in range(8)]
print(mixed_numbers)

#ex5
for i in range(1,21):
    print(i)

for index, x in enumerate(range(1,21)):
    if index % 2 == 0:
        print(x)

#ex6
user_name = input("what's your name")
my_name = 'Coco'
while user_name != my_name:
    user_name = input("what's your name")

print('Welcome!')

#ex7
user_fruit = input('please input a few fruits with a single space in between')
user_fruit_list = user_fruit.split()
print(user_fruit_list)
test_fruit = input('please type in your chosen fruit today :) ')
if test_fruit in user_fruit_list:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('you chose a new fruit. i hope you enjoy')


#ex8
toppings_list = []
toppings = input("what toppings do you want to add?(type 'quit' to exit)")
while toppings.lower() != 'quit':
    print('you will get that topping!')
    toppings_list.append(toppings)
    toppings = input("what toppings do you want to add?(type 'quit' to exit)")

price = 10 + 2.5 * len(toppings_list)
print(f'here is what you have ordered: {toppings_list} and here is the total price ${price}')

#ex9
under3 = 0
child12 = 10
teenage13 = 15

total_price = 0

while True:
    user_age = int(input('type in your age: (type 0 to finish)'))

    if user_age == 0:
        break 

    if user_age < 3:
        total_price += under3
    elif 3 <= user_age <= 12:
        total_price += child12
    else:
        total_price += teenage13

print(f'here is the total price : {total_price}')

teenagers = input('enter the makes and spilt with spaces: ').split()
allowed = teenagers.copy()

for name in teenagers:
    age = int(input(f'please enter your age: {name} '))

    if 16 <= age <= 21:
        allowed.remove(name)

print(allowed)


#ex10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while 'Pastrami sandwich'in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

finished_order = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) 
    print(f"I made your {current_sandwich}.")
    finished_order.append(current_sandwich)

print('ready!')


