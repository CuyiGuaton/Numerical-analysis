#!/usr/bin/env python
# coding: utf-8

from math import *
from collections import deque

def f(x):
    #return sqrt(6*x-1)/3
    #return sqrt(10-x**3)/2
    return sqrt((9*x**3 + x)/6)

def a(x,y,z):
    return (y**2 -x*z)/(2*y-x-z)

queue = deque([0,0,0])
aitken=0
i=1
j=1
count = 0
z=0.3
cosa=0.3
print('\\begin{tabular}{|c|c|c|} \n \hline')
print('Iteración & $x_k$  & Error \% \\\\ \hline')
print('0 &  {} &  \\\\ \hline'.format(z))
while i<31:
    x = f(z)
    y =abs(z-x)*100/abs(x)
    #print('i = ',  i, 'x = ' ,'{0:.50f}'.format(x),' error porcentual =', '{0:.50f}'.format(y))
    if count >= 3:
        aitken = a(queue[0],queue[1],queue[2])
        #print(' {0} {1} {2}').format(queue[0],queue[1],queue[2])
        print('{0}& {1:.50f} & {2:4f} \\\\ \hline'.format(j,aitken,abs(cosa- aitken)*100/abs( aitken) ))
        cosa = aitken
        j+=1
    queue.append(x)
    queue.popleft()
    #print(' {0}&  {1:.50f} & {2:.4f}  \\\\ \hline'.format(i,x,y,aitken))
    z=x
    count+=1
    i+=1
print('\\end{tabular} ')
