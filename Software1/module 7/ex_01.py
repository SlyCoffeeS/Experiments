import random

def roll_dice():
    return random.randint(1, 6)

while roll_dice != 6:
    result = roll_dice()
    print(result)

    if result == 6:
        break

    


