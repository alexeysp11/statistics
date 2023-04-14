"""
Plot the graph of a quadratic function.
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    x_q = np.arange(0, 10, 0.1)
    x_sin = np.arange(0, 3 * np.pi, 0.1)
    y_q = x_q**2 - 10*x_q + 20
    y_sin = 10 * np.sin(x_sin) + 5

    #plt.grid()
    #plt.xlabel('x axis label')
    #plt.ylabel('y axis label')
    plt.title('Diagram')

    plt.subplot(2,2,1)
    plt.plot(x_q, y_q)
    plt.legend(['Quadratic Equation'])
    plt.grid()

    plt.subplot(2,2,3)
    plt.plot(x_sin, y_sin)
    plt.legend(['Sine'])
    plt.grid()

    plt.subplot(2,2,2)
    plt.plot(x_q, y_q)
    plt.plot(x_sin, y_sin)
    plt.legend(['Quadratic Equation','Sine'])
    plt.grid()

    plt.show()

if __name__ == '__main__':
    main()
