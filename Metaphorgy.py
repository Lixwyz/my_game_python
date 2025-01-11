import random
import time
from helpers import *
from data import *



name = input("Привет путник, мечтаешь о путешествиях и захватывающих сражениях?\nТогда ты попал в нужное тебе место,\nскорее введи своё имя и иди очищать земли давно зарытой цивилизации в игре 'Эхо времени': ")
player["name"] = name
current_enemy = 0

while True:
    action = input('''Выберите действие: 
1 - в бой
2 - тренировка
3 - инфо об игроке 
4 - инфо о текущем противнике 
5 - Показать инвентарь 
6 - Магазин 
7 - Пойти в казино:  
''')
    print()
    if action == "1":
        current_enemy = fight(current_enemy)
        if current_enemy == len(enemies):
            print("Поздравляю, вы победили всех врагов")
            break
    elif action == '2':
        traininng_type = input('''1 - тренировать атаку
2 - тренировать защиту
''')
        training(traininng_type)
    elif action == '3':
        display_player()
        print()
    elif action == '4':
        display_enemy(current_enemy)
        print()
    elif action == '5':
        display_inventory()
        print()
    elif action == '6':
        shop()
        print()
    elif action == '7':
        earn()
        print()
    print()







