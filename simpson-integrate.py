from math import sqrt,sin

def faster_simpson( a, b, steps):
   h = (b-a)/float(steps)
   a1 = a+h/2
   s1 = sum( f(a1+i*h) for i in range(0,steps))
   s2 = sum( f(a+i*h) for i in range(1,steps))
   print(h)
   return (h/6.0)*(f(a)+f(b)+4.0*s1+2.0*s2)

def f(x):
    return sqrt(x)*(x-2)

print(faster_simpson(0, 5/2, 4))
