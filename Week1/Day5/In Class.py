shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]

for shirt in shirts: 
    print(shirt['name'])



sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
#del sample_dict['name']
#del sample_dict['salary']

keys_to_remove = ["name", "salary"] 
for key in keys_to_remove:
    del sample_dict[key]
    
print(sample_dict)