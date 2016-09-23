#!/usr/bin/env python
"""
A filter that transform text into lower case
"""
import fileinput

def process(line):
    print (line.lower().strip())
        
for line in fileinput.input():
    process(line)
