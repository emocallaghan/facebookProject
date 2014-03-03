# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:43:29 2014

@author: shrinidhit
"""

from swampy.TurtleWorld import *
from random import randint

def my_clone(oldturtle):
    newturtle = Turtle()
    newturtle.x = oldturtle.x
    newturtle.y = oldturtle.y
    newturtle.heading = oldturtle.heading
    return newturtle

def recursive_tree(turtle, branch_length, level):
    if level == 0:
        fd(turtle, branch_length)
#        newturtle = my_clone(turtle)
 #       newturtle.set_color('green')
    else:        
    #Main stem
        fd(turtle, branch_length)
    #Left branch
        alice_left = my_clone(turtle)
        lt(alice_left, randint(15,45))
        recursive_tree(alice_left, branch_length*randint(5,8)/10, level-1)
        alice_left.undraw()
    #Right branch
        bk(turtle, randint(1,7)/10)
        alice_right = my_clone(turtle)
        rt(alice_right, randint(15,45))
        recursive_tree(alice_right, branch_length*randint(5,8)/10, level-1)
        alice_right.undraw()

if __name__== '__main__':
    world = TurtleWorld()
    alice = Turtle()
    alice.delay = 0
    alice.lt()
    alice.bk(100)
    recursive_tree(alice, 100, 12)
    alice.undraw()
    wait_for_user()
    