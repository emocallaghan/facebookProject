# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:52:21 2014

@author: shrinidhit
"""

def rightjustify(mystring):
    if len(mystring)>70:
        print "not possible to right justify";
    else:
        lspace = 70 - len(mystring) #lspace = number of leading spaces needed
        print ' '*lspace + mystring;
mystring = raw_input('Enter your string:');
rightjustify(mystring);
    
    