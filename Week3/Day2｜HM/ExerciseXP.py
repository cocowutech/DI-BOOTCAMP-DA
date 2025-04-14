#EX1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#Create another cat breed named Siamese which inherits from the Cat class.
class Siamese(Cat):
    def sing(self,sounds):
        return f'{sounds}'
    
#Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
cat1 = Bengal('Luna',2)
cat2 = Chartreux('Milo',3)
cat3 = Siamese('Nala',1)

all_cats = [cat1,cat2,cat3]

#Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
sara_pets = Pets(all_cats)

#Take all the cats for a walk, use the walk method.
sara_pets.walk()

#Ex2
#Create a class called Dog with the following attributes name, age, weight.
class Dog():
    def __init__(self,name,age,weight):
        self.name = name 
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f'{self.name} is barking.'
    
    def run_speed(self):
        return self.weight/self.age*10
    
    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            winner = self.name
        else:
            winner = other_dog.name
        return f'The winner is {winner}!'


dog1 = Dog('Aa',1,10)
dog2 = Dog('Bb',3,8)
dog3 = Dog('Cc',5,14)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog3))

