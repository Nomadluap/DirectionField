#!/usr/bin/env python
from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np
from math import atan, pi, sqrt

BOTTOM_EXTENT = -10
TOP_EXTENT = 10
SAMPLES = 30

# y is a function of x. 
def dydx(x,y):
    return 3 - 2*y


def main():
    fig = plt.figure(num = 1)
    ax = fig.add_subplot(111)

    # create vector field
    X,Y = np.meshgrid(np.linspace(BOTTOM_EXTENT, TOP_EXTENT, SAMPLES),
                      np.linspace(BOTTOM_EXTENT, TOP_EXTENT, SAMPLES))
    U = 1
    V = dydx(X, Y)
    #normalize the arrows
    N = np.sqrt(U**2 + V**2)
    U2, V2 = U/N, V/N
    ax.quiver(X, Y, U2, V2)

    #show the plot
    plt.xlim([BOTTOM_EXTENT, TOP_EXTENT])
    plt.ylim([BOTTOM_EXTENT, TOP_EXTENT])
    plt.xlabel(r"$x$")
    plt.ylabel(r"$y(x)$")
    plt.show()


if __name__ == "__main__":
    main()
