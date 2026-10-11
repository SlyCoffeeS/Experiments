class Room:
    def __init__(self, name: str, item, enemy=None):
        self.name = name
        self.item = item
        self.enemy = enemy
        self.exits = {}

    def add_exit(self, direction: str , destination_room):

        self.exits[direction.lower()] = destination_room


    def get_exit(self, direction: str):  ## "get" error preventer, by checking if key is in dictionary

        return self.exits.get(direction.lower())

    def remove_item(self):

        collected = self.item
        self.item = None
        return collected

    def get_description(self):
        item_name = self.item.name if self.item else "None"
        enemy_name = self.enemy.name if self.enemy else "None"
        return f"\nLocation: {self.name} | Item: {item_name} Enemy: {enemy_name}\n"