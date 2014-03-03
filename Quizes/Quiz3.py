# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:25:39 2014

@author: shrinidhit
"""

def recursive_flatten(L_orig):
    L = []
    for i in range(len(L_orig)):
        if type(L_orig[i]) == list:
            L.extend(recursive_flatten(L_orig[i]))
        else:
            L.append(L_orig[i])
    return L
if __name__== '__main__':
    print recursive_flatten([1,[2,3,4,5], [1,2]])
        