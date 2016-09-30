#!/usr/bin/env python
# coding: utf-8
from math import *
from collections import deque

def f(x):
    return x*log10(x) -10
    #return 4*(0.4)**(-0.75)* log10( x**(1-0.5*0.4 ))  + 4*(0.4)**(-0.75)* log10( 6000  ) - 0.4* 0.4 **(-1.2) - x

#Se ingresan los valores entre los que está la raíz
queue = deque([20,50])
z = queue[1]
i=1
#se Itera 10 veces
while i <10:
    x = queue[1] - f(queue[1])*( queue[1] - queue[0] )/( f(queue[1]) - f(queue[0])  )
    print(' {0}&  {1:.5f} & {2:.5f}  \\\\ \hline'.format(i,x,abs(x-z)/abs(x)))
    z=x
    queue.append(x)
    queue.popleft()
    i+=1
