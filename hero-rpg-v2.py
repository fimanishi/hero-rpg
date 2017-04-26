#!/usr/bin/env python3

import mechanics.mech as mechanics

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    hero = mechanics.define_heroes()
    shadow = mechanics.define_test()

    mechanics.combat(hero, shadow)

if __name__ == "__main__":
  main()
