from authors import print_authors
from main import start_the_gameplay_scene
menu = "\n₪₪₪THE REBIRTH OF A PROGRAMMER₪₪₪\n\n" \
      "**START GAME(1)\n" \
      "**AUTHORS(2)\n"
print(menu)

try:
    scene = input(">>>")

    while True:
        if scene == "1":
            start_the_gameplay_scene()
        elif scene == "2":
            print_authors()
            scene = input(">>>")
        elif scene == "menu":
            print(menu)
            scene = input(">>>")
        else:
            print("Введи 1 или 2. Что сложного?")
            scene = input(">>>")

except KeyboardInterrupt:
    a = input("Вы точно хотите выйти?[y/n]: ")
    if a.lower() != "y":
        exit()
    else:
        pass