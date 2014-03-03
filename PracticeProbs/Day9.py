# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:45:17 2014

@author: shrinidhit
"""

#Class Activities, Day 9
def reverse_lookup(d, v):
    Values = []
    for k in d:
        if d[k] == v:
            Values.append(k)
    return Values
    
if __name__=='__main__':
    print reverse_lookup({"a":1,"b":2,"c":2}, 2)
            