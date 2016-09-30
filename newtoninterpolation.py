#!/usr/bin/env python
# coding: utf-8
from math import *
from collections import deque

#Esta es la finción a interpolar, aunque se pude interpolar pon puntos igual, hay que cambiar los f(xi) po yi
def f(x):
    return sin(sqrt(x))*(cos(x))**2
#diferencia divida
def divdef2(a, b):
    return f(a)/(a -b) + f(b)/(b-a)

def divdef3(x0,x1,x2):
    return f(x0)/( (x0-x1) * (x0-x2) ) + f(x1)/( (x1-x0) * (x1-x2)  ) + f(x2)/( (x2-x0) * (x2-x1)  )

def divdef4(x0,x1,x2,x3):
    return f(x0)/((x0-x1)*(x0-x2)*(x0-x3)) + f(x1)/((x1-x0)*(x1-x2)*(x1-x3)) + f(x2)/((x2-x0)*(x2-x1)*(x2-x3))+ f(x3)/((x3-x0)*(x3-x1)*(x3-x2))

# x2, x1,x0
def ww(x0,x1,x2):
    return divdef(x2, x1) + divdef(x2,x0) - divdef(x1,x0)

x0= 0
x1= pi/5
x2= 0.5
x3 = 0.2


print(' f(x0) = {0:.7f}, f(x1)= {1:.7f} f(x2) = {2:.7f} f(x3) = {3:.7f}'.format(f(x0), f(x1), f(x2), f(x3)  ) )
print(' {0:.5f} + {1:.5f}(x-{2:.5f}) '.format(f(x0), divdef2(x0,x1), x0  ) )
print('+ {0:.5f}(x-{1:.5f})(x-{2:.5f}) '.format(divdef3(x0,x1,x2), x0, x1  ) )
print('+ {0:.5f}(x-{1:.5f})(x-{2:.5f})(x-{3:.5f}) '.format(divdef4(x0,x1,x2,x3), x0, x1 , x2 ) )
#print('0 &  {} &  \\\\ \hline'.format(z))


#print(' {0}&  {1:.50f} & {2:.8f}  \\\\ \hline'.format(i,x,abs(x-z)/abs(x)))
