class Slime:
    def __init__(self, name, hp, drop_item=None):
        self.name = name
        self.hp = hp
        self.drop_item = drop_item

    def take_damage(self, amount):
        self.hp -= amount
        return self.hp <= 0
