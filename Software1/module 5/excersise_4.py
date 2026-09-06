import random

integer = random.randint(1, 10)

answer = float(input("Guess the right number (1-10) "))

while answer != integer:
    if answer > integer:
        print("too high.")
    elif answer < integer:
        print("too low.")
    answer = float(input("guess again"))
        
print("Correct")