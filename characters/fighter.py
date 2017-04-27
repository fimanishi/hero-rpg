#!/usr/bin/env python3

from characters.base import Character
from random import randint

class Fighter(Character):
    special_ability = "critical damage"
    def __init__(self, *args, criticalp = 25, critical = 2, **kwargs):
        super().__init__(*args, **kwargs)
        self.criticalp = criticalp  # percentage of chance of having a critical attack
        self.critical = critical    # multiplication factor
        self.prize = 8
        self.health = 10
        self.power = 4

    def attack(self, enemy):
        original = self.power
#        self.power = randint(1,5)
        p = randint(1,100)
        if p <= self.criticalp:
            self.power = round(self.power * self.critical)  # rounds the power value after the critical
        super().attack(enemy)                               # calls the attack function from the super class
        self.power = original
