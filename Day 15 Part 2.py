# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 23:58:31 2017

@author: James Jiang
"""

def next_a(n):
    num = (16807 * n) % 2147483647
    return(num)
    
def next_b(n):
    num = (48271 * n) % 2147483647
    return(num)
    
a = next_a(783)
b = next_b(325)
count = 0

list_a = []
list_b = []

while len(list_a) != 5000000:
    if a % 4 == 0:
        list_a.append(a)
    a = next_a(a)
    
while len(list_b) != 5000000:
    if b % 8 == 0:
        list_b.append(b)
    b = next_b(b)
 
for i in range(5000000):
    if (list_a[i] % 2**16) == (list_b[i] % 2**16):
        count += 1
        
print(count)