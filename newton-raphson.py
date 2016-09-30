#!/usr/bin/env python
# coding: utf-8

#Investigue y aplique el método de Newton, describa dos métodos, al menos, para obtenerlo. Obtener un método iterativo que sea capaz de aproximar el valor. Aplíquelo para aproximar dicho valor con tres iteraciones. Confeccione una tabla de resultados
#http://docs.sympy.org/dev/tutorial/calculus.html
#http://lybniz2.sourceforge.net/safeeval.html
#http://pybonacci.org/2012/04/18/ecuaciones-no-lineales-metodo-de-biseccion-y-metodo-de-newton-en-python/
#http://pybonacci.org/2012/04/30/como-calcular-limites-derivadas-series-e-integrales-en-python-con-sympy/
#http://blog.crespo.org.ve/2015/02/calculo-de-derivadas-con-sympy.html
#from sympy import *
#x = Symbol('x')
#diff(x**2)

from math import *

def f(x):
    #return x**(1/math.sqrt(5))-5.2
    #return 19.4098*x**2 -0.0125*x-2
    #return x**3 - 6*x**2 + 11*x - 6.1
    return x*log10(x) -10
def df(x):
    #return math.sqrt(5)*x**(math.sqrt(5)/5)/(5*x)
    #return (38.8196)*x -(0.0125)
    #return 3*x**2 -  12*x + 11
    return (log(x) + 1)/log(10)
i=1
z=8
print('\\begin{tabular}{|c|c|c|} \n \hline')
print('Iteración & $x_k$  & Error \% \\\\ \hline')
print('0 &  {} &  \\\\ \hline'.format(z))

while(i<8):
    x= z-f(z)/df(z)
    e=abs(z-x)*100/abs(x)
    print('{0} &  {1:.7f}  & {2:.5f} \\\\ \hline'.format(i,x,e))
    z=x
    i+=1
print('\\end{tabular} ')
