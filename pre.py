#!/usr/bin/env python
# coding: utf-8
from mpmath import *

def f(x):
    z = (float(x))
    y=(0.5*log(5,2)) #el log es al revéz de como esta en wolfram(wolfram lotiene como log(2,5))
    z =x - y
    return z

1.160964047443681173935159714744695087932415696512290306027378197907967388304312607925069871679685077549828

i=1
z = float(10.0)
x = float(1.0)
y = float(1.0)
print('\\begin{tabular}{|c|c|c|} \n \hline')
print('Iteración & $x_k$  & Error \% \\\\ \hline')
print('0 &  {} &  \\\\ \hline'.format(z))
while i<6:
    x = (z - f(z)**2/(f(z + f(z)) - f(z)))
    y =(z-x)*100/x
    #print('i = ',  i, 'x = ' ,'{0:.50f}'.format(x),' error porcentual =', '{0:.50f}'.format(y))
    print(' {0}&  {1} & {2} \\\\ \hline'.format(eval(repr(mpf(i))),eval(repr(+mpf(x))),eval(repr(y))))
    z=x
    i+=1
print('\\end{tabular} ')
