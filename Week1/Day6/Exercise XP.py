#ex1 
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary1 = dict(zip(keys, values))
print(dictionary1)

#ex2
toddler = 0
kid = 10
teenager = 15
total_price = 0

#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#bonus:

family = {}
num_members = int(input('How many family members are buying tickets?'))
for _ in range(num_members):
    name = input("enter the person's name")
    age = int(input(f'enter the age of {name}'))
    family[name] = age

for name, age1 in family.items():
    if age1 < 3:
        price = toddler
    elif 3<= age1 <= 12:
        price = kid
    else:
         price = teenager
    print(f"{name} needs to pay ${price}")
    total_price += price 

print(total_price)


#ex3
# Step 1: Creating the dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],  
    "international_competitors": ["Gap", "H&M", "Benetton"],  
    "number_stores": 7000,
    "major_color": { 
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]  
    }
}

# Step 2: Print dictionary to verify
print(brand)

brand["number_stores"] = 2

for client in brand["type_of_clothes"]:
    print(f"zara's client is {client}")

brand['country_creation'] = 'Spain'
print(brand)

if "international_competitors" in brand:
    brand["international_competitors"].append('Desigual')


del brand["creation_date"]

print(brand["international_competitors"][-1])

print(brand["major_color"]['US'])

print("Number of key-value pairs:", len(brand))

print("Keys in the dictionary:", list(brand.keys()))

more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 10000 
}

brand.update(more_on_zara)

print("Updated number of stores:", brand["number_stores"])

#Exercise 4 : Disney characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
for user in users:
    disney_users_A[user] = users.index(user)
print(disney_users_A)

disney_users_B = {}

for i in range(len(users)):
    disney_users_B[i] = users[i]
print(disney_users_B)


print(sorted(users))