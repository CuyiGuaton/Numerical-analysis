import numpy as np
from scipy.misc import comb
from matplotlib import pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    puntos = entrada()
    npuntos= len(puntos)
    xpuntos = [p[0] for p in puntos]
    ypuntos = [p[1] for p in puntos]
    xvalor, yvalor = bezier(puntos,100000 )
    plt.plot(xvalor, yvalor,)
    plt.plot(xpuntos, ypuntos, "ro")
    for xy in zip(xpuntos, ypuntos):
        ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
    plt.show()

def beizerpol(i, n, t):
    """
     The Bernstein polynomial of n, i as a function of t
    """

    return comb(n, i) * ( t**(i) ) * (1 - t)**(n-i)


def bezier(puntos, saltos):
    """
       Given a set of control puntos, return the
       bezier curve defined by the control puntos.

       puntos should be a list of lists, or list of tuples
       such as [ [1,1],
                 [2,3],
                 [4,5], ..[Xn, Yn] ]
        saltos is the number of time steps, defaults to 1000

        See http://processingjs.nihongoresources.com/bezierinfo/
    """

    npuntos = len(puntos)
    xpuntos = np.array([p[0] for p in puntos])
    ypuntos = np.array([p[1] for p in puntos])

    t = np.linspace(-0.2, 1.2, saltos)

    polinomio = np.array([ beizerpol(i, npuntos-1, t) for i in range(0, npuntos)   ])
    xvalor = np.dot(xpuntos, polinomio)
    yvalor = np.dot(ypuntos, polinomio)

    return xvalor, yvalor

def entrada():
    A=[]
    archivo=open('puntos.txt','r')
    fila =0
    for linea in archivo:
        A.append([])
        for i in linea.split(' '):
            A[fila].append(float(i))
        fila += 1
    archivo.close()
    return A

if __name__ == "__main__":
    main()
