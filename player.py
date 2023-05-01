import sys
import os
import mob
from time import sleep


class Player(mob.Mob):
    def __init__(self, karma, **kwargs):
        self.karma = karma
        super().__init__(**kwargs)

    def attack(self):

        count = 1
        max_len = 30
        time_interval = 0.7
        stripe = " "
        damage_coefficient = max_len / 2

        print("---Выберите атаку---")
        for i in self.inventory:
            print(f"{count}.{i} -- урон = {self.inventory[i]}")
            count += 1

        print("Для атаки нужно нажать на сочетание клавиш Ctrl + C")
        while True:
            try:
                result = int(input(">>>")) - 1
                key = list(self.inventory)
                key[result]
                break;
            except:
                print("Неправельно введён номер")

        print(" " + "." * 29 + "|")
        try:
            for i in range(max_len):
                stripe += "█"
                print(stripe, end='\r')
                time_interval *= 0.85
                sleep(time_interval)
        except KeyboardInterrupt:
            pass

        print("")
        if len(stripe) == max_len + 1:
            return [key[result], 0]
        else:
            return [key[result], round(self.inventory[key[result]] * len(stripe) / damage_coefficient, 2)]

    def addItems(self, item: str, damage: int):

        print(f"В ваш инвентарь добавлена - {item} : урон - {damage}")
        self.inventory[item] = damage

    def death(self):
        pass