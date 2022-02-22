import matplotlib.pyplot as plt
import numpy as np


def show_graph(bx, by, f, points):
    if isinstance(f, list):
        return __show_graph2(bx, f)

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


def __show_graph2(bx, f):
    x1 = np.linspace(-bx, bx, 100)
    x2 = np.linspace(-bx, bx, 100)
    f1 = np.zeros((x1.size, x2.size))
    f2 = np.zeros((x1.size, x2.size))

    for kf, g in enumerate((f1, f2)):
        for i, deta in enumerate(x2):
            for j, beta in enumerate(x1):
                g[j, i] = f[kf](beta, deta)

    X, Y = np.meshgrid(x1, x2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, f1)
    ax.plot_surface(X, Y, f2)
    plt.show()
