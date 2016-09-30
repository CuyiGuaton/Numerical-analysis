#!/usr/bin/env python
# coding: utf-8

import scipy as scipy
from scipy.interpolate import lagrange
from math import sin,sqrt,pi,cos

def f(x):
    return sin(sqrt(x))*(cos(x))*(cos(x))

x=[0,0.2,0.5,pi/5]
y=[f(0),f(0.2),(0.5),f(pi/5)]
#Devuelbe ax**3 + bx**2 + cx + d
print(scipy.interpolate.lagrange(x,y))


#Evalua el polinomio en 0.5
p=scipy.interpolate.lagrange(x,y)
print(p(0.5))
