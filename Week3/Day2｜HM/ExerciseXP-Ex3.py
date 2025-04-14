from ExerciseXP import Dog
import random

class PetDog(Dog):
    def __init__(self, name ,age, weight):
        super().__init__(name,age,weight)
        self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *dog_names):
        all_names = ', '.join(dog_names)
        print(f"{all_names} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet.")
    
dog1 = PetDog("Charlie", 3, 10)
dog2 = PetDog("Buddy", 4, 12)
dog3 = PetDog("Max", 2, 8)

dog1.play(dog1.name, dog2.name, dog3.name)  # all play together
dog1.train()
dog1.do_a_trick()  # 随机输出一个特技
