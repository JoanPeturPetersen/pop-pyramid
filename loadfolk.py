#-*- coding: utf-8 -*-

from scipy import *

# Load folkatal data

def parse_ar(s):
    return 1

def parse_tal(s):
    if s=='-':
        return 0
    else:
        return int(s)

converters = {0: parse_ar}
for i in range(1, 28): # Just add enough
    converters[i] = parse_tal

data = loadtxt('folk_tils.csv', delimiter='\t', skiprows=4, converters=converters)
konufolk = loadtxt('konufolk.csv', delimiter='\t', skiprows=4, converters=converters)
mannfolk = loadtxt('mannfolk.csv', delimiter='\t', skiprows=4, converters=converters)
munur = mannfolk - konufolk
