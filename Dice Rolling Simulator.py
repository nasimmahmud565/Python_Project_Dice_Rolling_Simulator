import random

def roll_dice():
    return random.randint(1, 6)

num_rolls = int(input('Enter the number of times to roll the dice: '))

for _ in range(num_rolls):
    print('Roll:', roll_dice())
