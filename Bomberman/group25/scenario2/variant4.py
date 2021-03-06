# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster
from scen2var3character import Scen2Var3Character


# TODO This is your code!
sys.path.insert(1, '../group25')
from scenario2_AStarCharacterWithBomb import TestCharacter
# from scen2var4character import Scen2Var4Character

# Create the game
random.seed(20) # TODO Change this if you want different random choices
g = Game.fromfile('map.txt')
g.add_monster(SelfPreservingMonster("aggressive", # name
                                    "A",          # avatar
                                    3, 13,        # position
                                    2             # detection range
))

# TODO Add your character
"""
g.add_character(TestCharacter("me", # name
                              "C",  # avatar
                              0, 0  # position
))
"""
g.add_character(TestCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                              False,
                              7, 7
))

# Run!
g.go()
