import matplotlib.pyplot as plt
import numpy as np


def show_graph(bx, by, f, points):
    vf = np.vectorize(f)
    x = np.linspace(-bx, bx, 100)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    plt.grid(True)
    plt.xlim((-bx, bx))
    plt.ylim((-by, by))

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.plot(x, vf(x), 'g', label='y=f(x)')
    ax.plot(*list(zip(*points)), 'ro')

    plt.show()
