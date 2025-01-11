import random
import time
from data import *

def fight(current_enemy):
    baff_attack = "3"
    if items in player["inventory"]:
        baff_attack = input("Желаете выпить зелье силы?\n1 - Да\n2 - Нет")
    
    
    round = random.randint(1, 2)

    enemy  = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]["hp"]
    print(f"{enemy['name']}: {enemy['script']}")
    print()
    input("Нажмите ENTER, чтобы продолжить")
    while player["hp"] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f"{player['name']} атакует {enemy['name']}")
            crit = random.randint(1, 100)
            if crit < player["luck"]:
                 enemy_hp -= player["attack"] * 3
            else:
                enemy_hp -= player["attack"]
            time.sleep(1)
            print(f'''{player['name']} - {player['hp']}
{enemy['name']} - {enemy_hp}.''')
            print()
            time.sleep(1)
        else:
            print(f"{enemy['name']} атакует {player['name']}")
            player['hp'] -= enemy['attack'] * player["armor"]
            time.sleep(1)
            print(f"{player['name']} - {player['hp']}\n{enemy['name']} - {enemy_hp}.")
            print()
            time.sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f"Противник - {enemy['name']}: {enemy['win']}")
        current_enemy += 1   
    else:
        print(f"{enemy['name']}: {enemy['loss']}")
    player["hp"] = 100
    return current_enemy

def training(traininng_type):
    skip = "2"
    if "Пропуск тренировки" in player["inventory"]:
        skip = input("Желаете пропустить тренировку?\n1 - Да\n2 - Нет:\n ")
    if skip == "2":
        print("Тренировка успешно пропущена!:)")
        for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')
            time.sleep(1.5)
    if traininng_type == '1':
        player['attack'] += 2
        print(f' Тренировка окончена! Теперь ваша сила атки: {player["attack"]}')
    elif traininng_type == '2':
         player['armor'] -= .09
         print(f"Тренировка завершена! Теперь броня поглощает: {100 - player['armor'] * 100}% урона")
    print()

def display_player():
    print("Вы, путник который ищет мести за свою жену Элизабет")
    print(f"Игрок - {player['name']}")
    print(f"Сила атаки - {player['attack']}. Шанс критического урона ({player['attack']}ед.) равен {player['luck']}%")
    print(f"Брона поглощает {(1 - player['armor']) * 100}% урона")


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Сила атаки - {enemy["attack"]}') 
    print(f'Здоровье {enemy["name"]} - {enemy["hp"]}')
    


def display_inventory():
    print("У вас есть:")
    for value in player["inventory"]:
        print(value)
    print(f"У вас {player['money']} монет")
    print()
    if "Зелье удачи" and "Зелье силы" in player['inventory']:
        wish_of_potions = input("Напишите название зелья которое хотите выпить: ")
        print()
        if wish_of_potions == "Зелье удачи":
            if "Зелье удачи" in player["inventory"]:
                potion = input("Желаете выпить зелье удачи? ")
                print()
                if potion == "Да":
                    player["luck"] += 9 
                    print(f"Теперь шанс нанести критический урон равен: {player['luck']}%")
                    player["inventory"].remove("Зелье удачи")
        print()
        if wish_of_potions == "Зелье силы":
            if "Зелье силы" in player["inventory"]:
                attack_potion = input("Желаете выпить зелье силы? ")
                print()
                if attack_potion == "Да":
                    player["attack"] += 5
                    print("Теперь сила атаки увеличена на 5 едениц")
                    player["inventory"].remove("Зелье силы")
        print()
    if "Клон" in player['inventory']:
        clone = input("Желаете использовать клона который удвоит все ваши харрактеристики? ")
        print()
        if clone == "Да":
            print("Усиление навыков...")
            player['attack'] += 2
            player['luck'] *= 2
            player['armor'] *= 2
            player['hp'] *= 2
            player["inventory"].remove("Клон")
            print("Вот ваши харрактеристики после баффа: ")
            print()
            print(f"Ваша защита: {player['armor']}")
            print(f"Ваше здоровье: {player['hp']}")
            print(f"Ваша сила атаки: {player['attack']}")
            print(f"Ваша удача: {player['luck']}")
    print()



def shop():
    print(f"Добро пожаловать, {player['name']}")
    print(f"У тебя есть {player['money']} монет")
    for key, value in items.items():
        print(f"{key} - {value['name']}: {value['price']}")

    item = input()
    if item in player['inventory']:
        print(f"У тебя уже есть {items[item]['name']}")
    elif player['money'] >= items[item]['price']:
        print(f"Ты успешно приобрёл {items[item]['name']}")
        player['inventory'].append(items[item]['name'])
        player['money'] -= items[item]['price']
    else:
        print("Мне не хватает монет, пойду работать :(")
        print()
        print(f"Буду ждать тебя снова {player['name']} ")

def earn():
    game = input("Добро пожаловать на завод по производству денег,\nУ тебя есть шанс 65% заработать 500 монет, и шанс 35% потерять их, желаю удачи!\nИли же есть вторая игра, всё или ничего где с шансом 60% вы можете получить x2 к вашим деньгам, или потерять всё с шансом 40%!\nВведите игру в которую хотите поиграть: 1, или 2!\n")
    if game == "1":
        result = random.randint(1, 100)
        time.sleep(1.5)
        print("Вы....")
        time.sleep(1.5)
        print("Страшно????")
        time.sleep(1.5)
        if result <= 65:
            print("Вы выиграли 500 монет!")
            player["money"] += 500   
        else:
            print("Вы проиграли, спасибо за ваши деньги:)")
            player["money"] -= 500 
            print()
            print(f"Ваш баланс: {player['money']}")
    if game == "2":
        result = random.randint(1, 100)
        time.sleep(1.5)
        print("Вы....")
        time.sleep(1.5)
        print("Боитесь??")
        time.sleep(1.5)
        if result <= 60:
            print("Вы удвоили свои деньги!")
            player["money"] *= 2
        else:
            print("Вы проиграли, спасибо за ваши деньги:)")
            player["money"] -= player["money"]
            print()
    print(f"Ваш баланс: {player['money']}")