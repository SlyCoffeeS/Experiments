import json
import os
from game.entities.item import Item
from game.world.room import Room
from game.entities.player import Player
from game.entities.enemy import Slime

base_dir = os.path.dirname(__file__)

## creating items and rooms and enemies

#items
sword = Item("Sword", 1.5)
shield = Item("Shield", 4)
slime_gel = Item("Slime gel", 0.1)
gold_pouch = Item("Gold pouch", 1)
bronze_key = Item("Bronze Key", 0.2)

#enemies
blue_slime = Slime("Blue Slime", hp=20, drop_item=slime_gel)
king_slime = Slime("Boss fight: King Slime", hp=45, drop_item=bronze_key)

## rooms
dungeon1 = Room("Floor 1", item=gold_pouch)
dungeon2_west = Room("Floor 2 - Slime Cave", enemy=blue_slime, item=gold_pouch)
dungeon2_east = Room("Floor 2 - Armory", item=sword)
dungeon2_main = Room("Floor 2 - Main hall", item=gold_pouch)
dungeon3 = Room("Floor 3 - Slime Nest", enemy=king_slime, item=gold_pouch)
dungeon4 = Room("Floor 4 - Dungeon Exit", item=None)
# Connecting rooms
dungeon1.add_exit("left", dungeon2_west)
dungeon2_west.add_exit("back", dungeon1)

dungeon1.add_exit("right", dungeon2_east)
dungeon2_east.add_exit("back", dungeon1)

dungeon1.add_exit("up", dungeon2_main)
dungeon2_main.add_exit("down", dungeon1)

dungeon2_main.add_exit("up", dungeon3)
dungeon3.add_exit("down", dungeon2_main)

dungeon3.add_exit("up", dungeon4)
dungeon4.add_exit("down", dungeon3)

## my simple battle function
def battle_slime(player):
    room = player.location
    enemy = room.enemy

    if enemy == None: ## checking for enemies
        print("\nNo enemies nearby!\n")
        return

    has_sword = any(item.name.lower() == "sword" for item in player.items) ## adding a use for the sword
    if has_sword:
        damage = 10
    else:  # or if u dont have a sword
        damage = 5

    enemy.hp -= damage
    print(f"\n You hit the {enemy.name} for {damage}! (Remaining Hp: {max(0,enemy.hp)})")

    if enemy.hp <= 0:
        print(f"{enemy.name} has been defeated!")
        if enemy.drop_item:
            room.item = enemy.drop_item
            print(f"{enemy.name} dropped a {enemy.drop_item.name} on the floor!")
        room.enemy = None

def read_file_safe(filename): # helper function for opening/ Reading text files and error handling when necessary
        filepath = os.path.join(base_dir, filename)
        try:
            with open(filepath, "r") as file:
                intro_text = file.read()
            print(intro_text)
        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error occured while handling the file.")

def game_save(player): # saving game and what to save
    save_path = os.path.join(base_dir, "save.json")
    save_data = {
    "name": player.name,
    "room": player.location.name,
    "inventory": [item.name for item in player.items]
    }
    with open(save_path, "w") as file:
        json.dump(save_data, file) # converts into json and writes to file
        
        print("\nGame saved!\n")
def load_game(): ## loading and what to load
    save_path = os.path.join(base_dir, "save.json")
    try:
        with open(save_path, "r") as file:
            data = json.load(file)
        room_map = {
            "Floor 1": dungeon1,
            "Floor 2 - Slime Cave": dungeon2_west,
            "Floor 2 - Armory": dungeon2_east,
            "Floor 2 - Main Hall": dungeon2_main,
            "Floor 3 - Slime Nest": dungeon3,
            "Floor 4 - Dungeon Exit": dungeon4,
        }
        starting_room = room_map.get(data["room"], dungeon1)

        loaded_player = Player(data["name"], items=[], location = starting_room)

        item_map =  {

            "Sword": sword,
            "Shield": shield,
            "Slime gel": slime_gel,
            "Gold pouch": gold_pouch,
            "Bronze Key": bronze_key

            }
        for item_name in data ["inventory"]:
            if item_name in item_map:
                loaded_player.items.append(item_map[item_name])
        print(f"\nWelcome back, {loaded_player.name}!")
        return loaded_player
    except FileNotFoundError: ## if no save file
        return None

def open_inventory(player): # checking inventory 

    print("\nInventory contains")

    if player.items:
        for item in player.items:
            print(f"- {item.name} ({item.weight} kg )")

    else:
        print("\nNo items in inventory!\n")

def drop_item(player): # dropping itemes
    drop_name = input("\n what would you like to drop")
    for item in player.items: # looking thorugh inventory
       if item.name.lower() == drop_name.lower():
           player.items.remove(item)
           player.location.item = item
           print(f"\n You have tossed {item.name} in the corner at {player.location.name}\n")
           return
    else:
        print("\nNo such item in inventory\n")
    
           


def exploration_menu(player): # sub menu
    while True:
        print("1. Move (up / down)")
        print("2. Look around")
        print("3. Take item in room")
        print("4. Slay the slime")
        print("5. Toss item in a corner")
        print("6. Return to Main menu")
        

        choice = input("Choose an action: ")

        if choice == "1":
            direction = input("\nwhere do you wanna go? (up/down/left/right/back)\n").lower()
            if direction == "up" and player.location.name == "Floor 3 - Slime Nest": # cant Win, without putting in the work yk. Checks if you have defated the boss before trying to leave.
                if player.location.enemy != None:
                    print("\n The King Slime blocks the way out, Defeat it to escape!\n")
                    continue
            player.move(direction)
            if player.location.name == "Floor 4 - Dungeon Exit": # Win condition to beat the game.
                print("\n Congratulations! You have reached the end!\n")
                break

        elif choice == "2":
            print(player.location.get_description())

        elif choice == "3":
            player.collect_item()

        elif choice == "4":
            battle_slime(player)               

        elif choice == "5":
            drop_item(player)

        elif choice == "6":
                    print("\nReturning to Main menu\n")
                    break

def main_menu(player): # as it says. Main menu
    while True:
        print("\n Main menu ")
        print("1. Explore")
        print("2. Open inventory")
        print("3. Random options (Greet/count)")
        print("4. Read instructions")
        print("5. Save game")
        print("6. Lopeta")

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
             read_file_safe("instructions.txt")

        elif command == "5":
            game_save(player)
        
        elif command == "6":
                    print("\ncatch ya later\n")
                    break


player = None # meaning no player created or loaded
save_path = os.path.join(base_dir, "save.json")
if os.path.exists(save_path):
    choice = input("Saved game found! (yes) to continue. press enter to skip.)").lower() # up to you if u wanna continue
    if choice in ["yes"]:
        player = load_game()

if player is None:
    read_file_safe("intro.txt")
    name=input("Insert your name: ")
    try:
        age = int(input("Insert your age: "))
    except ValueError:
        age = 0
    if age >= 12: # age checking if you are old enough to fight the war.
        print(f"Welcome {name}!")
        player = Player(name, items=[], location=dungeon1,)
    else:
        print ("user is a minor, Come back when older")
        exit()

main_menu(player)