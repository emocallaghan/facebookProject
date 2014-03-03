# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:40:07 2014

@author: shrinidhit
"""
import math;
from math import pi
from unum import Unum

#Unum.reset()

from unum.units import *

#Problem1
r = 5; #takes in radius
volume = (4.0/3.0) * pi * r**3; #finds volume
print volume;

#Problem2
dollars = Unum.unit('dollars');
cents = Unum.unit('cents', .01 * dollars);


bookprice = 24.95 * dollars; #rcost of each book
shipping = 75 * cents; #shipping cost of each book
cost = (bookprice * 60) + 3*dollars + 59*shipping; #finds bookstore's cost
print cost.asUnit(dollars)

#Problem3
starttime = 6*h + 52*min
easypace = (8*h + 15*min)/(1*mile)
fastpace = (7*h + 12*min)/(1*mile)

endtime = starttime + easypace*1*mile + fastpace*3*mile + easypace*1*mile;
print endtime;