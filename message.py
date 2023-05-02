def print_message(person_name, massege_body):
    print(f"---{person_name}-------------------------------------------------")
    print(f"→ {massege_body}")
    input()


def choosing_an_action(actions):
    print("----------------------------------------------------\nВыбери действий")
    count = 1
    for key in actions:
        print(count, key)
        count += 1

    result = return_choosing_result(len(actions))
    print(list(actions.keys())[result])
    actions[list(actions.keys())[result]]()


def return_choosing_result(len):
    while True:
        try:
            result = int(input(">>>"))
            if 0 < result <= len:
                return result - 1
        except:
            print("Неправельно введён номер")

def print_title(string: str):
    print(f"---- {string} ----")
