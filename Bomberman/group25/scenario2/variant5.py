# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
sys.path.insert(1, '../group25')
from testcharacter import TestCharacter
from scen2var5character import Scen2Var5Character

# Create the game
random.seed(223) # TODO Change this if you want different random choices
g = Game.fromfile('map.txt')
g.add_monster(StupidMonster("monster", # name
                            "S",       # avatar
                            3, 5,      # position
))
g.add_monster(SelfPreservingMonster("monster", # name
                                    "A",       # avatar
                                    3, 13,     # position
                                    2          # detection range
))

# TODO Add your character
"""
g.add_character(TestCharacter("me", # name
                              "C",  # avatar
                              0, 0  # position
))
"""
g.add_character(Scen2Var5Character("me", # name
                              "C",  # avatar
                              0, 0,  # position
                              3 # depth
))

# Run!
g.go()
