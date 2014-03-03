# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:24:27 2014

@author: shrinidhit
"""

def sum_of_squares(n):
    sum = 0 #initializes sum value
    for i in range(1,n+1):
        sum = sum + (i**2)
    return sum

def filter_out_negataive_numbers(list):
    newlist = [] #initializes new list to be returned
    for i in range(len(list)):
        if list[i] >= 0:
            newlist.append(list[i])
    return newlist