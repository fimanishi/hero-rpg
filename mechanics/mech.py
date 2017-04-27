#!/usr/bin/env python3

from characters.base import Character
from characters.fighter import Fighter
from characters.zombie import Zombie
from characters.medic import Medic
from characters.shadow import Shadow
import random

c_dict = {"Fighter": Fighter, "Medic": Medic, "Shadow": Shadow}#, "Zombie": Zombie()}


def heroes_menu():
    print("="*80)
    print("{:^80}".format("Welcome to Honey Badger's RPG Game!"))
    print("="*80)
    print()
    print("Let's start! Please choose a character number!")
    print()
    j = 1
    c_list = []
    for i in c_dict.values():
        i = i()
        print("{counter}. {name:10} - Health: {health:<3} - Power: {power:<3} - Special ability: {special_ability}".format(
        counter=j, name=i.name, health=i.health, power=i.power, special_ability=i.special_ability))
        c_list.append(i)
        j += 1
    while True:
        print()
        try:
            choice = int(input("Select your character's number: "))
            if choice >= 1 and choice <= len(c_dict):
                print()
                user_name = input("Please choose a name: ")
                user = c_list[choice-1]
                if user_name != "":
                    user.name = user_name
                print()
                print("Welcome {}, you are a {}! Good luck!".format(user.name, user.__class__.__name__))
                print()
                user.user = True
                return user
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")


def choose_enemy():
    enemy = random.choice(list(c_dict.keys()))
    return c_dict.pop(enemy)()


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
