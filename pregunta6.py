#!/usr/bin/env python
# coding: utf-8
#\item El método de Steffensen presenta una convergencia rápida y presenta además, la ventaja adicional de que el proceso de iteración sólo necesita un punto inicial. Este método calcula el siguiente punto de iteración a partir de la expresión: $$ x_{n+1} = x_n - \dfrac{[f(x)]^2}{f(x_n + f(x_n)) - f(x_n)} $$
from math import *
from decimal import *

def f(x):
    z = Decimal(float(x))
    #y= Decimal(log(sqrt(5),2)) #el log es al revéz de como esta en wolfram(wolfram lotiene como log(2,5))
    #z =x - y
    z = 2**x - Decimal(sqrt(5))
    return z

1.160964047443681173935159714744695087932415696512290306027378197907967388304312607925069871679685077549828

getcontext().prec = 50
i=1
z = Decimal(float(1.0))
x = Decimal(float(1.0))
y = Decimal(float(1.0))
print('\\begin{tabular}{|c|c|c|} \n \hline')
print('Iteración & $x_k$  & Error \% \\\\ \hline')
print('0 &  {} &  \\\\ \hline'.format(z))
while i<7:
    x = Decimal(z - f(z)**2/(f(z + f(z)) - f(z)))
    #y =(z-x)*100/x
    y= f(z + f(z)) - f(z)
    #print('i = ',  i, 'x = ' ,'{0:.50f}'.format(x),' error porcentual =', '{0:.50f}'.format(y))
    print(' {0}&  {1:.35f} & {2:.30f} \\\\ \hline'.format(i,x,y))
    z=x
    i+=1
print('\\end{tabular} ')
