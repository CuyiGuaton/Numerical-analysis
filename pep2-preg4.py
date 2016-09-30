from math import *

def f(x,w):
    return 2*w*exp(-2*(2*x + 5))

x1=-sqrt((3-2*sqrt(6/5))/7)
x2=sqrt((3-2*sqrt(6/5))/7)
x3 = -sqrt((3+2*sqrt(6/5))/7)
x4 = sqrt((3+2*sqrt(6/5))/7)

w1=(18+sqrt(30))/36
w2 = (18-sqrt(30))/36


print( (f(x1,w1) + f(x2,w1) + f(x3,w2) + f(x4,w2) ))
