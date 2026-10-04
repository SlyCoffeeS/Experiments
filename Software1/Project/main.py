import json
from game.entities.item import Item
from game.world.room import Room
from game.entities.player import Player

sword = Item("Sword", 1.5)
shield = Item("Shield", 4)
carrot_seed = Item("Carrot seeds", 0.2)
leather_cap = Item("Leather cap", 0.4)

dungeon1 = Room("Floor 1", item=sword)
dungeon2 = Room("Floor 2", item=carrot_seed)
dungeon3 = Room("Floor 3", item=shield)
dungeon4 = Room("Floor 4", item=leather_cap)

dungeon1.add_exit("up", dungeon2)
dungeon2.add_exit("down", dungeon1)

dungeon2.add_exit("up", dungeon3)
dungeon3.add_exit("down", dungeon2)

dungeon3.add_exit("up", dungeon4)
dungeon4.add_exit("down", dungeon3)

# def add_item():
#     what = input("What would you like to add to the inventory?")

#     inventory.append(what)
#     print(f"\n{what} has been added to inventory\n")
    
def open_inventory(player):

    print("\nInventory contains")

    if player.items:
        for item in player.items:
            print(f"- {item.name} ({item.weight} kg )")

    else:
        print("\nNo items in inventory!\n")

def drop_item(player):
    drop_name = input("\n what would you like to drop")
    for item in player.items:
       if item.name.lower() == drop_name.lower():
           player.items.remove(item)
           player.location.item = item
           print(f"\n You have tossed {item.name} in the corner at {player.location.name}\n")
           return
    else:
        print("\nNo such item in inventory\n")
    
           


def exploration_menu(player):
    while True:
        print("1. Move (up / down)")
        print("2. Look around")
        print("3. Take item in room")
        print("4. Toss item in a corner")
        print("5. Return to Main menu")
        

        choice = input("Choose an action: ")

        if choice == "1":
            direction = input("\nwhere do you wanna go? (up/down)\n")
            player.move(direction)

        elif choice == "2":
            print(player.location.get_description())

        elif choice == "3":
            player.collect_item()
                                
        elif choice == "4":
            drop_item(player)

        elif choice == "5":
                    print("\nReturning to Main menu\n")
                    break

def main_menu(player):
    while True:
        print("\n Main menu ")
        print("1. Explore")
        print("2. Open inventory")
        print("3. Random options (Greet/count)")
        print("4. Read instructions")
        print("5. Lopeta")

        command = input("\nWhat would you like to do?\n")

        if command == "1":
            exploration_menu(player)
        elif command == "2":
            open_inventory(player)
        elif command == "3":
            print("\n Random stuff")
            print("a) greet")
            print("b) count")
        
            random = input("Choose 'a' for Greet/ 'b' for Count")
            
            if random == "a":
                print(f"\nTere!, kuidas laheb?")
            elif random == "b":
                print("\n1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
            else:
                print("\nBad choice")

        elif command == "4":
             with open("instructions.txt", "r") as file:
                  instructions_txt = file.read()
                  print(instructions_txt)
        
        elif command == "5":
                    print("\ncatch ya later\n")
                    break


try:
    with open("intro.txt", "r", encoding="utf-8") as file:
        intro_text = file.read()
        print(intro_text)
except FileNotFoundError:
     print("File not found.")
except IOError:
     print("Error occured while handling the file.")


name=input("Insert your name: ")
age=int(input("insert your age: "))
print(name)
print(age)

if age >= 12:
    print(f"Welcome {name}!")
    player = Player(name, items=[], location=dungeon1,)
    main_menu(player)
else:
    print ("user is a minor, Come back when older")
