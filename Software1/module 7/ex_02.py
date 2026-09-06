import random

sides = int(input("Enter how many sides the dice should have:"))
def roll_dice(sides):
    return random.randint(1, sides)

while roll_dice != sides:
    result = roll_dice(sides)
    print(result)

    if result == sides:
        break