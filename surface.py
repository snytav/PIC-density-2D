import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def plot_3Dsurface(x_space,y_space,surface2,x_name,y_name,name):
    # fig = plt.figure()
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    X, Y = np.meshgrid(x_space, y_space)
    surf = ax.plot_surface(X, Y, surface2, rstride=1, cstride=1, cmap=cm.viridis,
                           linewidth=0, antialiased=False)

    # ax.set_xlim(0, 1)
    # ax.set_ylim(0, 1)
    # ax.set_zlim(0, 3)

    fig.colorbar(surf, ax=ax)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name);
    plt.title(name)
    plt.savefig(name+'.png')
