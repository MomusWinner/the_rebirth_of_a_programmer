import mob
import random


class Enemy(mob.Mob):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def attack(self):
        i = random.randint(0, len(self.inventory) -1)
        key = list(self.inventory)
        return [key[i],self.inventory[key[i]]]

    def death(self):
        pass