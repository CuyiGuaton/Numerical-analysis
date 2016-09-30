#!/usr/bin/env python
# coding: utf-8
from math import sqrt

def f(x,y):
    return sqrt(y)/(2*x+1)
    #return sin(x) - log(y)

#f es la función, x e y valores inciales, xf el valor al que se quiere llegar y n los saltos para lograrlo
def euler(f,x,y,xf,n):
    x0=x
    h= (xf-x)/float(n)
    print('h = {0}'.format(h))
    for i in range(1, n+1):
        y = y + h*f(x,y)
        x = x + h
        print('{0} &  {1:.2f}  & {2:.6f}' .format( i, x, y))


#euler(0.13,0.32,0.14,4)
euler(f,0,4,2,4)
