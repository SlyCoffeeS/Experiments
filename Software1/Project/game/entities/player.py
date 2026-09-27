class Player:
    def __init__(self, name, items, location):
        self.name = name
        self.items = []
        self.location = location


    def move(self, direction: str):

        if direction in self.location.exits:
            self.location = self.location.exits[direction]
            print(f"\nYou moved to the {self.location.name}.\n")
        else:
            print("\nYou can't move in that direction!\n")


    def collect_item(self):

        if self.location.item:
            item = self.location.remove_item()
            self.items.append(item)
            print(f"\n You collected {item.name}, {item.weight} kg!\n")
        else:
            print("\nNothing to collect here\n")

    