# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:27:21 2014

@author: shrinidhit
"""
from swampy.TurtleWorld import *

def my_triangle(turtle, side_length):
    rt(turtle)
    fd(turtle, side_length/2)
    for i in range(3):
        rt(turtle, 120)
        fd(turtle, side_length)
    bk(turtle, side_length/2)
    lt(turtle)

if __name__== '__main__':
    world = TurtleWorld()
    alice = Turtle()
    my_triangle(alice,100)
    wait_for_user()
    