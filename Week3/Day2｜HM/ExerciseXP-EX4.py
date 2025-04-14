class Family():
    def __init__(self,last_name):
        self.members = []
        self.last_name = last_name
    
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f'congrats on the family member:{kwargs['name']}')
    
    def is_18(self, name):
        for person in self.members:
            if person['name'] == name:
                return person['age'] >= 18
        return False
    
    def family_presentation(self):
        print(f"\n The {self.last_name} family members are:")
        for person in self.members:
            print(f" - {person}")

# 创建一个 Family 实例
my_family = Family("Smith")

# 添加初始成员
my_family.born(**{'name':'Michael','age':35,'gender':'Male','is_child':False})
my_family.born(**{'name':'Sarah','age':32,'gender':'Female','is_child':False})

print("Michael:", my_family.is_18("Michael"))   # True
print("Sarah:", my_family.is_18("Sarah")) # False

my_family.family_presentation()


class TheIncredibles(Family):
    def __init__(self,last_name):
        super().__init__(last_name)
    
    def use_power(self,name):
        for person in self.members:
            if person['name'] == name:
                print(f"{name}'s power is {person['power']}")
            else: 
                raise Exception(f'{name} is not over 18 and cannot use their power.')

    def incredible_presentation(self):
            print("Here is our powerful family")
            super().family_presentation()

incredibles = TheIncredibles("Incredibles")

initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

for person in initial_members:
    incredibles.born(**person)

incredibles.incredible_presentation()

incredibles.born(name="Baby Jack", age=1, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")

incredibles.incredible_presentation()