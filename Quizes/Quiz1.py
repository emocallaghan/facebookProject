# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:21:53 2014

@author: shrinidhit
"""
#Quiz 1

#Problem 1:
from unum.units import *;
mowrate = (100.0/5) * (m**2 /min);
print mowrate.asUnit(m**2/h)

#Problem 3:
def hinge(n):
    if n < 0:
        return 0;
    else:
        return n;

#Problem 4:
def print_number_of_days(n):
    if n == 1:
        print "Input is 1 day"
    else:
        print "Input is " + str(n) + " days"