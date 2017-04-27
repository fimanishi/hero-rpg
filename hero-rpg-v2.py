#!/usr/bin/env python3

import mechanics.mech as mechanics

from characters.shadow import Shadow

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    user = mechanics.heroes_menu()
    enemy = mechanics.choose_enemy()


    mechanics.combat(user, enemy)

if __name__ == "__main__":
  main()
