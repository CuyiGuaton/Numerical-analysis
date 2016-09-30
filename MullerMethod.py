#!/usr/bin/env python
# coding: utf-8
from math import *
from collections import deque

def f(x):
        return x**2 - exp(-x)

def divdef(a, b):
    return f(a)/(a -b) + f(b)/(b-a)

def divdefgrand(x0,x1,x2):
    return f(x0)/( (x0-x1) * (x0-x2) ) + f(x1)/( (x1-x0) * (x1-x2)  ) + f(x2)/( (x2-x0) * (x2-x1)  )

# x2, x1,x0
def ww(x0,x1,x2):
    return divdef(x2, x1) + divdef(x2,x0) - divdef(x1,x0)


#           x0,x1,x2
queue = deque([-1,0,2])

i=3
w= ww(queue[0],queue[1],queue[2])
z=queue[2]
i=1
print('\\begin{tabular}{|c|c|c|} \n \hline')
print('Iteración & $x_k$  & Error \% \\\\ \hline')
#print('0 &  {} &  \\\\ \hline'.format(z))
while i <10:
    w= ww(queue[0],queue[1],queue[2])
    raiz = sqrt(w**2 - 4*f(queue[2])*divdefgrand(queue[2],queue[1],queue[0]))
    if w - raiz > w+ raiz:
        x = queue[2]- 2*f(queue[2])/( w - raiz)
    else:
        x = queue[2] -2*f(queue[2])/( w + raiz)
    print(' {0}&  {1:.50f} & {2:.8f}  \\\\ \hline'.format(i,x,abs(x-z)/abs(x)))
    z=x
    queue.append(x)
    queue.popleft()
    i+=1
print('\\end{tabular} ')
