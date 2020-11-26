# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 01:02:55 2020

@author: anwar adam
"""

# Simple Pylab Example

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(1**3)
    myExponential.append(1.5**i)
    
plt.plot(mySamples, myLinear)

plt.plot(mySamples, myQuadratic)

plt.plot(mySamples, myCubic)

plt.plot(mySamples, myExponential)

