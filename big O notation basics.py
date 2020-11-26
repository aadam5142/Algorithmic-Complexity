# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:40:44 2020

@author: anwar
"""

# Big O Notation

def fact_iter(n):
    """assumes n an int >=0"""
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

# Law of Addition for O()

for i in range(n):
    print('a')
for j in range(n*n):
    print('b')
    
# Law of Multiplication of O()

for i in range(n):
    for j in range(n):
        print('a')
        
    