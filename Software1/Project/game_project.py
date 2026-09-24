## crazy to start making a game before knowing what the game -
## - is going to be even about
inventory = []

def add_item():
    what = input("What would you like to add to the inventory?")

    inventory.append(what)
    print(f"\n{what} has been added to inventory")
    
def open_inventory():

    print("\nInventory contains")

    for item in inventory:
        print("- " + item)

def drop_item():
    drop = input("\nWhat item would you like to drop?")

    if drop in inventory:

        inventory.remove(drop)
        print(f"\n{drop} has been dropped on the floor.")

    else:
        print("\ncant drop something thats not there!")



def main_menu():
    while True:
        print("\n Main menu ")
        print("1. Add item")
        print("2. Open inventory")
        print("3. Drop item")
        print("4. Lopeta")
        print("\n Fun menu")
        print("5. Greet")
        print("6. count")

        command = input("What would you like to do?")

        if command == "1":
            add_item()
        elif command == "2":
            open_inventory()
        elif command == "3":
            drop_item()
        elif command == "4":
            print("catch ya later")
            break
        elif command == "5":
            print(f"\nTere!, kuidas laheb?")
        
        elif command == "6":
            print("\n1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

name=input("Insert your name: ")
age=int(input("insert your age: "))
print(name)
print(age)

if age >= 12:
    print(f"Welcome {name}!")
    main_menu()
else:
    print ("user is a minor, Come back when older")
