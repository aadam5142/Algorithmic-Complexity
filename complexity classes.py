# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:48:23 2020

@author: anwar
"""

# Logarithmic Complexity

def intToStr(i):
    digits = '0123456789'
    if i = 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result

# Linear Complexity

def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

# Linear Complexity 2

def fact_iter(n):
    for in in range(1, n+1):
        prod *= i
    return prod

# O() for recursive factorial

def fact_recur(n):
    """ assume n >= 0 """
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n - 1)
    
# Quadratic Complexity

def isSubset(L1, L2):
    for el in L1:
        matched = False
        for e2 in L2:
            if el == e2:
                matched = True
                break
            if not matched:
                return False
    return True

# Quadratic Complexity

def intersect(L1, L2):
    tmp = []
    for el in L1:
        for e2 in L2:
            if el == e2:
                tmp.append(el)
                
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res

# O() for nested loops

def g(n):
    """ assume n >= 0 """
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x

# Exponential Complexity

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]] # list of empty list
    
    smaller = genSubsets(L[:-1]) # all subsets without last element
    
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element
        
    return smaller + new

# Tricky Complexity

def h(n):
    """ assume n an int >= 0"""
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
        return answer

# Complexity of Iterative Fibonacci

def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii 
            fib_ii = tmp + fib_ii 
        return fib_ii 
  
#Complexity of recursive fibonacci

def fib_recur(n):
    """assumes n an int >= 0"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)
    