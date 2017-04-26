#!/usr/bin/env python3

from characters.base import Character
from characters.fighter import Fighter
from characters.zombie import Zombie
from characters.medic import Medic
from characters.shadow import Shadow

    # hero = Hero(name = "hero", health = 10, power = 5)
    # goblin1 = Character(name = "goblin", health = 6, power = 2)
    # zombie = Zombie(power = 1)
    # medic = Medic(health = 10, power = 2, heal = 2)
    # shadow = Shadow(power = 1)


def heroes_menu():
    return Fighter(name = "Test")




def print_playing_menu(enemy):
    while True:
        print()
        print("What do you want to do?")
        print("1. fight {}".format(enemy.name))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        try:
            if int(inpt) > 0 and int(inpt) < 4:
                break
            else:
                print("Invalid inpt {}".format(inpt))
        except ValueError:
            print("Invalid inpt {}".format(inpt))
    return inpt


def define_heroes():
    return Fighter(name = "hero", health = 10, power = 5)

def define_test():
    return Medic(health = 10, power = 2, heal = 2)

def combat(hero, enemy):
    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        inpt = print_playing_menu(enemy)
        if inpt == "1":
            hero.attack(enemy)
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        if enemy.alive():
            enemy.attack(hero)
