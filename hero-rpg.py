#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True

class Hero(Character):
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print("The goblin is dead.")

    # def alive(self):
    #     if self.health > 0:
    #         return True

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    def attack(self, enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")

    # def alive(self):
    #     if self.health > 0:
    #         return True

    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

def main():
    #hero_health = 10
    #hero_power = 5
    #goblin_health = 6
    #goblin_power = 2

    hero = Hero(10, 5)
    goblin1 = Goblin(6, 2)

    while goblin1.alive() and hero.alive():
        hero.print_status()
        goblin1.print_status()
        # print("You have {} health and {} power.".format(hero.health, hero.power))
        # print("The goblin has {} health and {} power.".format(goblin1.health, goblin1.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            # Hero attacks goblin
            hero.attack(goblin1)
            #goblin1.health -= hero.power
            #print("You do {} damage to the goblin.".format(hero.power))
            #if goblin1.health <= 0:
                #print("The goblin is dead.")
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin1.alive():
            # Goblin attacks hero
            #hero.health -= goblin1.power
            #print("The goblin does {} damage to you.".format(goblin1.power))
            #if hero.health <= 0:
            #    print("You are dead.")
            goblin1.attack(hero)

if __name__ == "__main__":
  main()
