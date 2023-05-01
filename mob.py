from abc import ABC, abstractmethod


class Mob(ABC):
    def __init__(self, name, inventory, health):
        self.name = name
        self.inventory = inventory
        self.health = health

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def death(self):
        pass