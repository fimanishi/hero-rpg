#!/usr/bin/env python3

from characters.base import Character
from random import randint

class Medic(Character):
    special_ability = "healing"
    def __init__(self, *args, heal = 2, healp = 20, **kwargs):
        super().__init__(*args, **kwargs)
        self.heal = heal    # number of health points to be healed
        self.healp = healp  # percent chance of healing
        self.prize = 5      # character's bounty value
        self.health = 10
        self.power = 2

    def post_attack(self):
        p = randint(1,100)
        if p <= self.healp:
            self.health += self.heal
            print("The {} recuperated {} health points.".format(self.name, self.heal))
