#!/usr/bin/env python
"""
A filter that split lines of text into one word per line
"""
import fileinput

import re

def process(line):
    l = re.split('\W+', line)
    for x in l:
        if len(x) >= 2:
            print(x)
            
for line in fileinput.input():
    process(line)