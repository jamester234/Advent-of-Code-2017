# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:07:33 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Day 23 Data.txt')]

total = 0
dummy = 0    

for i in range(len(all_lines)):
    counter = 0
    for j in range(len(all_lines[i])):
            for k in range(len(all_lines[i])):
                digits_j = [a for a in all_lines[i][j]]
                digits_k = [a for a in all_lines[i][k]]
                digits_j.sort()
                digits_k.sort()
                if digits_j != digits_k:
                    counter += 1
    if counter == (len(all_lines[i])**2 - len(all_lines[i])):
        total += 1
        
print(total)
