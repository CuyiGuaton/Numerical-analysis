#!/usr/bin/env python
# coding: utf-8
from math import *

def f(x):
    return sqrt(x)*(x-2)

def trapezoidal( a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    print('h = {0}'.format(h))
    print('{0} &  {1:.5f}  & {2:.5f}' .format( i,b, h*s))

trapezoidal(0,2.5,4)
