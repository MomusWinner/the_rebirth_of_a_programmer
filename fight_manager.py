from enemy import Enemy
from player import Player


def fight(player:Player,enemy:Enemy):
    print("---Бой---")
    print(f"*-- {player.name} vs {enemy.name} --*")

    player_health = player.health
    enemy_health = enemy.health
    while True:
        player_attack = player.attack()
        enemy_attack = enemy.attack()

        print(f"\nАтака - {player_attack[0]}| Урон - {player_attack[1]}")

        enemy_health -= player_attack[1]
        print(f"Вражеское здоровье - {round(enemy_health,2)}")

        print(f"\nАтака - {enemy_attack[0]}| Урон - {enemy_attack[1]}")

        player_health -= enemy_attack[1]
        print(f"Ваше здоровье - {round(player_health,2)}")

        if enemy_health <= 0:
            print(f"Вы победили {enemy.name}")
            return
        elif player_health <= 0:
            print("\n---Попробуйте ещё раз!---\n")
            player_health = player.health
            enemy_health = enemy.health