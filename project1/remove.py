#!/usr/bin/env python
"""
remove top 10 stop words from Little Women
"""
import fileinput
import re

stopwords = ['and','the','to','of','her','it','in','you','she','for']

def process(line):
    l = re.split('\W+', line)
    for i in l:
        if i not in stopwords and len(i)>=2:
            print (i)

for line in fileinput.input():
    process(line)
