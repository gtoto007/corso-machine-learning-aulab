import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

def plane(w,x1,x2,y):
    # Plot the plane
    MARGIN = 0
    plt.rcParams["figure.figsize"] = (10,10)
    edges_x = [np.min(x1) , np.max(x1) + MARGIN]
    edges_y = [np.min(x2) , np.max(x2) + MARGIN]
    # Plot the axes
    sns.set(rc={"axes.facecolor": "white", "figure.facecolor": "white"})
    ax = plt.figure().gca(projection="3d")
    ax.set_xlabel("Prenotazioni", labelpad=15, fontsize=30)
    ax.set_ylabel("Temperatura", labelpad=15, fontsize=30)
    ax.set_zlabel("Cornetti", labelpad=5, fontsize=30)

    # Plot the data points
    ax.scatter(x1, x2, y, color='b')

    plt.savefig('plot.png', dpi=300)


    xs, ys = np.meshgrid(edges_x, edges_y)

    zs = np.array([w[0] + x * w[1] + y * w[2] for x, y in
                  zip(np.ravel(xs), np.ravel(ys))])
    ax.plot_surface(xs, ys, zs.reshape((2, 2)), alpha=0.2)
    #ax.view_init(40, 10)

    plt.tight_layout()
    plt.tight_layout() 
    plt.savefig('plot_plane.png', dpi=300)
    plt.show()
    