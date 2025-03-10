import random
def number_guessing_game():
    random_number = random.randint(1,100)
    max_attempts = 7 
    for attempt in range(max_attempts):
        number = int(input("Enter your number"))
        if number < random_number:
            print("Too low!")
        elif number > random_number:
            print("Too high!")
        else:
            print("congrats!")
            return
    
    print(f"Game Over! The correct number was {random_number}.") 
    
number_guessing_game()