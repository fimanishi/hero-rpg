#!/usr/bin/env python3

# base class for all characters
class Character:

    def __init__(self, name = "", health=0, power = 0, power_range=[], prize = 0, dodge = 0, user = False):
        self.name = name                # takes a string that represents the character's name
        if not self.name:               # checks if a name was given, if not gives it its class' name
            self.name = self.__class__.__name__
        self.health = health            # takes an integer that represents the character's health
        self.power = power              # will be removed
        self.prize = prize              # takes an integer that represents the character's bounty
        self.dodge = dodge              # takes an integer that represents the probability of dodging in percent
        self.power_range = power_range  # takes a list with two integers that represents the
                                        # maximum and minimum damage
        self.user = user                # identifies if the character is the user

    # checks if the health of the character is greater than zero
    def alive(self):
        if self.health > 0:
            return True

    # function to be called by the character classes that possesses some ability after being attacked
    def post_attack (self):
        pass

    # prints the messages of the damage inflicted and checks if the enemy is alive. if not, prints that it's dead
    def print_damage(self, enemy):
        if self.user == True: # checks if the attacker is the user
            print("You do {} damage to the {}.".format(self.power, enemy.name))
            if not enemy.alive():
                print("The {} is dead.".format(enemy.name))
        elif self.user == False: # checks if the character being attacked is the user
            print("The {} does {} damage to you.".format(self.name, self.power))
            if not enemy.alive():
                print("You are dead.")

    # prints the message in case the character is able to dodge an attack
    def print_dodge(self, enemy):
        if self.user == True: # checks if the attacker is the user
            print("The {} dodged the attack".format(enemy.name))
        elif enemy.user == False: # checks if the character being attacked is the user
            print("You dodged the attack.")

    # attacks the enemy
    def attack(self, enemy):
        dodged = enemy.post_attack() # checks if the enemy dodged, if yes returns True
        if not dodged:
            enemy.health -= self.power
            self.print_damage(enemy)
        else:
            self.print_dodge(enemy)

    # prints the current health and power of the user and the enemy
    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))
