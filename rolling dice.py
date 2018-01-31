import random

min=1
max=6
roll_again = "yes"

while roll_again=="yes":
    print("Player1")
    print(random.randint(min,max))
    print("Player2")
    print(random.randint(min,max))

    roll_again=input("Do you want to roll again?\n")

