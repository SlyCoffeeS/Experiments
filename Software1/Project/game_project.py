## crazy to start making a game before knowing what the game -
## - is going to be even about

name=input("Insert your name: ")
age=int(input("insert your age: "))
print(name)
print(age)

menu = "select option\n1. greet\n2. count\n3. lopeta."

if age < 12:
    print ("user is a minor, Come back when older")
elif age >= 12:
    print(f"Welcome {name}!")
command = input(f"What shall we do now? {menu}")


while age >= 12:
    if command == "lopeta":
        break

    elif command == "greet":
        print(f"Tere!, kuidas laheb?")
        

    elif command == "count":
        print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

    select = input(menu)
    command = input("Anything else you would like to do?")

