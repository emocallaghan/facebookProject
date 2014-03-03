# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:43:01 2014

@author: shrinidhit
"""
from math import *;
#Function to calculate hypotenuse
def hypotenuse(a,b):
    c = sqrt(a**2 + b**2)
    print c
#Getting input to calculate hypotenuse
a = raw_input('Enter one side of triangle:');
b = raw_input('Enter other side of triangle:');
#Calculating hypotenuse
hypotenuse(float(a), float(b));