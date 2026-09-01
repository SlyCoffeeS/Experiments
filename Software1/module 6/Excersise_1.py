import random

rolls = int(input("how many dice to roll: "))

sum = 0
for roll in range(rolls):
    sum = sum + random.randint(1, 6)

print(f"sum of the dice: {sum}")