#!/usr/bin/env python3

from characters.base import Character
from random import randint

class Shadow(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 1 # character's health
        self.prize = 8  # character's bounty value
        self.dodge = 90 # chance in percent of dodging

    def post_attack(self):
        p = randint(1,100)
        if p > self.dodge:
            return False
        else:
            return True
