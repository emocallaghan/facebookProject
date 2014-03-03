# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:13:38 2014

@author: shrinidhit
"""

def get_complementary_base(base):
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'G':
        return 'C'
    elif base == 'C':
        return 'G'
    else:
        print 'bad input'
def is_between(x,y,z):
    return y<z and y>x
def factorial(n):
    ans = 1;
    for i in range(1, n+1):
        ans = ans * i
    return ans;
            