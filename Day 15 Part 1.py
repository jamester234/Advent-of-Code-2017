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
x = 0

while x < 40000000:
    if (a % 2**16) == (b % 2**16):
        count += 1
    a = next_a(a)
    b = next_b(b)
    x += 1
    
print(count)