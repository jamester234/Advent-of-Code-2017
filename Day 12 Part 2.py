# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 00:26:20 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Day 12 Data.txt')]

all_connections = []

for i in range(len(all_lines)):
    chars = [j for j in all_lines[i]]
    while True:
        if ' ' in chars:
            chars.remove(' ')
        else:
            break
    
    index = chars.index('-')
    chars[index] = ','
    connections = []
    counter = 0
    dummy = 0
    for k in range(len(chars)):
        if (chars[k] != ',') and (dummy == 0):
            connections.append(chars[k])
            dummy = 1
        elif (chars[k] != ',') and (dummy != 0):
            connections[counter] += chars[k]
        else:
            counter += 1
            dummy = 0
    connections = [int(k) for k in connections]
    all_connections.append(connections)

def group(n):
    master = []
    master.extend(all_connections[n])
    memory = []
    while True:
        for i in range(len(all_connections)):
            for j in range(len(all_connections[i])):
                if all_connections[i][j] in master:
                    for k in range(len(all_connections[i])):
                        if all_connections[i][k] not in master:
                            master.append(all_connections[i][k])
        if len(master) not in memory:
            memory.append(len(master))
        else:
            return(master)
            
all_groups = []
all_groups.append(group(0))
            
for i in range(len(all_connections)):
    for j in range(len(all_groups)):
        if all_connections[i][0] in all_groups[j]:
            break
    else:
        all_groups.append(group(all_connections[i][0]))
        
print(len(all_groups))