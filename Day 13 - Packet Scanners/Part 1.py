# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:06:08 2017

@author: James Jiang
"""

def position(range_firewall, time):
    offset = time % (2 * (range_firewall - 1))
    if offset > range_firewall - 1:
        return(2 * (range_firewall - 1) - offset)  
    else:
        return(offset)

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

ranges = {}

for pair in all_lines:
    chars = [i for i in pair]
    depth_firewall = ''
    range_firewall = ''
    x = 0
    while chars[x] != ':':
        depth_firewall += chars[x]
        x += 1
    x += 1
    for i in range(x, len(chars)):
        range_firewall += chars[i]
    ranges[int(depth_firewall)] = int(range_firewall)

severity = 0

for i in ranges:
    if position(ranges[i], i) == 0:
        severity += ranges[i] * i
        
print(severity)
