# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:07:33 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

total = 0
dummy = 0    

for i in range(len(all_lines)):
    counter = 0
    for j in range(len(all_lines[i])):
            for k in range(len(all_lines[i])):
                if all_lines[i][j] != all_lines[i][k]:
                    counter += 1
    if counter == (len(all_lines[i])**2 - len(all_lines[i])):
        total += 1
        
print(total)
