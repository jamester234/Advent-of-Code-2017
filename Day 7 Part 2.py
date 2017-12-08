# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:14:40 2017

@author: James Jiang
"""
all_lines = [line.rstrip('\n') for line in open('Day 7 Data.txt')]
        
all_lines_characters = []
for line in all_lines:
    characters = line.split()
    all_lines_characters.append(characters)
    
def weight(str):
    characters = [i for i in str]
    del characters[0]
    del characters[-1]
    output = ''
    for i in characters:
        output += i
    return(int(output))
    
def fixed(str):
    chars = [i for i in str]
    if ',' in chars:
        del chars[-1]
    str_2 = ''
    for j in chars:
        str_2 += j
    return(str_2)
    
def above_list(list):
    output = []
    output_true = []
    if len(list) == 2:
        return(output)
    for i in range(len(list)):
        if list[i] == '->':
            start = i + 1
            break
    for j in range(start, len(list)):
        output.append(list[j])
    for program in output:
        output_true.append(fixed(program))
    return(output_true)
    
weights_dict = {}
for i in range(len(all_lines_characters)):
    weights_dict[all_lines_characters[i][0]] = weight(all_lines_characters[i][1])
   
programs_dict = {}
for i in range(len(all_lines_characters)):
    if len(all_lines_characters[i]) > 2:
        programs_dict[all_lines_characters[i][0]] = above_list(all_lines_characters[i])
    
def sum_weight(key1):
    key = fixed(key1)
    weights = 0
    if key1 not in programs_dict:
        return(weights_dict[key])
    else:
        for program in programs_dict[key]:
            program_2 = fixed(program)
            weights += sum_weight(program_2)
        weights += weights_dict[key]
        return(weights)    

current = all_lines_characters[0][0]
index = 0  

while True:
    for i in range(0, len(all_lines_characters)):
        current_other = current + ','
        if (current in all_lines_characters[i]) and (i != index):
            current = all_lines_characters[i][0]
            index = i
            break
        elif (current_other in all_lines_characters[i]) and (i != index):
            current = all_lines_characters[i][0]
            index = i
            break
    else:
        bottom = current
        break
 
current_program = bottom
while True:
    sum_weights = {}
    dummy = 0
    for program in programs_dict[current_program]:
        sum_weights[program] = sum_weight(program)
    check_list = programs_dict[current_program]
    check = sum_weight(check_list[0])
    for program in check_list:
        program_2 = fixed(program)
        if sum_weight(program_2) != check:
            counter1 = [[check, check_list[0]]]
            counter2 = []
            for program_check in check_list:
                if sum_weight(program_check) != check:
                    counter2.append([sum_weight(program_check), program_check])  
                else:
                    counter1.append([sum_weight(program_check), program_check])
            if len(counter1) == 1:
                current_program = counter1[0][1]
            if len(counter2) == 1:
                current_program = counter2[0][1]
            dummy += 1    
    if dummy == 0:
        culprit = current_program
        break
   
list_weights_culprit1 = []
list_weights_culprit2 = []
for i in programs_dict:
    if culprit in programs_dict[i]:
        for j in programs_dict[i]:
            if sum_weight(j) != sum_weight(culprit):
                list_weights_culprit1.append(sum_weight(j))
            else:
                list_weights_culprit2.append(sum_weight(j))

delta = list_weights_culprit1[0] - list_weights_culprit2[0]   

print(weights_dict[culprit] + delta)
