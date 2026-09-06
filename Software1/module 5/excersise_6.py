import random

point = int(input("How many random points to generate? "))

cicrle_points = 0
count = 0

while count < point:
    x = random.uniform(-1, 1)
    t = random.uniform(-1,1)

    if x**2 + t**2 < 1:
        cicrle_points += 1

    count += 1

pi_approx = 4 * cicrle_points / point
print(f"Approximation of pi: {pi_approx}")