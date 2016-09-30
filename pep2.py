#!/usr/bin/env python
# coding: utf-8

from math import *
def f(x):
    z = float ((x**3 + 9*x)/(3*(x**2 + 1)))
    return z



i=0
z=1
while i<4:
    x = f(z)
    y =abs(z-x)*100/abs(x)
    print('i = ',  i, 'x = ' ,'{0:.5f}'.format(x),' error porcentual =', '{0:.4f}'.format(y))    #print(' {0}&  {1:.50f} & {2:.4f}  \\\\ \hline'.format(i,x,y,aitken))
    z=x
    i+=1
