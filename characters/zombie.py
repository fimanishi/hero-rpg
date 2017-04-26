#!/usr/bin/env python3

from characters.base import Character

class Zombie(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def alive(self):
        self.health = 0
        return True #zombie will never die
