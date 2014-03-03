# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:04:35 2014

@author: shrinidhit
"""

f = open("filename.txt", "r")
full_text = f.read
f.close
import re

boiler_plate_end = full_text.index( " ***")
end_of_novel = full_text.index("End of Project Gutenberg")
full_text = full_text[boiler_plate_end + 4:end_of_novel]
len(re.findall("a+", full_text)) #more than one a search
len(re.findall("\w+", full_text)) #breaks words
len(re.findall("[a-zA-Z'_0-9]+", full_text)) #breaks words including apostrophes
len(re.findall("[\w'\-]+", full_text)) #breaks words including apostrophes

