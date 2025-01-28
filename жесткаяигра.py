#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Студент
#
# Created:     23.09.2024
# Copyright:   (c) Студент 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print(f"Поприветствуйте героя -> {self.name}")
        print(f"Уровень здоровья: {self.health}")
        print(f"Класс брони: {self.armor}")
        print(f"Сила удара: {self.power}")
        print(f"Оружие: {self.weapon}\n")

    def strike(self, enemy):
        print(f"-> УДАР! {self.name} атакует {enemy.name}, используя {self.weapon}!")
        print(f"{self.name} вбивает свой {self.weapon} в противника!")
        enemy.armor -= self.power

        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

        print(f"{enemy.name} покачнулся от удара.")
        print(f"Класс брони упал до {enemy.armor}. Уровень здоровья снизился до {enemy.health}.\n")

        if enemy.health <= 0:
            print(f"===================")
            print(f"{enemy.name} был повержен!")
            print(f"===================")
            return True
        return False

    def heal(self, heal_amount):
        self.health += heal_amount
        print(f"{self.name} использует зелье исцеления на {heal_amount} здоровья!")
        print(f"Теперь уровень здоровья {self.name} составил {self.health}.\n")


def print_story():
    print("В далекой стране, в королевстве школы, разразилась война между благородными учениками и чудовищным директором.")
    print("Старый Директор, одержимый силой, завоевал все вокруг и теперь угрожает мирным ученикам.")
    print("Два отважных ученика, готовы противостоять ему и вернуть мир в королевстве школы.")
    print("Собираясь с силами, они стремятся одержать победу над Директором и защитить свой ум.\n")


knight = Hero('Ученик 1', 180, 25, 30, 'Мел')
rascal = Hero('Ученик 2', 150, 15, 25, 'Рогатка')
dragon = Hero('Директор', 500, 0, 45, 'Степлер')

print_story()

knight.print_info()
rascal.print_info()
dragon.print_info()


count = 1
while knight.health > 0 and rascal.health > 0 and dragon.health > 0:
    print(f"Раунд {count}")
    count += 1
    kring = random.choice([1, 2, 3])

    if kring == 1 and knight.health > 0:
        if knight.strike(dragon):
            break
    elif kring == 2 and rascal.health > 0:
        if rascal.strike(dragon):
            break
    elif kring == 3:
        if dragon.health > 0:
            if knight.health > 0 and random.choice([True, False]):
                if dragon.strike(knight):
                    break
            elif rascal.health > 0:
                if dragon.strike(rascal):
                    break


    for hero in [knight, rascal]:
        if hero.health > 0 and random.choice([True, False]) and hero.health < 100:
            heal_amount = random.randint(15, 30)
            hero.heal(heal_amount)


# Checking if at least one student is dead
if knight.health <= 0 or rascal.health <= 0:
    print("Директор вырывает заслуженную победу!")
else:
    print("Ученики одержали победу, и мир вернулся в королевстве школы!")