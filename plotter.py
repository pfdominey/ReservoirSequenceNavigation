import pandas as pd
import math
from plotnine import *
import matplotlib.pylab as plt
import matplotlib.patches as patches


def create_maze():
    angles = [22.5/180*math.pi+i*math.pi/4 for i in range(0,9)]
    radius = 1.0 / math.cos(22.5/180*math.pi)
    x = [radius*math.cos(angle) for angle in angles]
    y = [radius*math.sin(angle) for angle in angles]
    return pd.DataFrame({'x': x, 'y': y})


# ===============  LAYER DRAWERS =============================
def set_defaults(kwargs, defaults):
    for k, v in defaults.items():
        if k not in kwargs:
            kwargs[k]=v


def plot_new():
    return plt.figure().subplots()


def plot_maze(data=None, plot=None, **kwargs):
    set_defaults(kwargs, {'color': 'k'})
    if data is None:
        data = create_maze()
    return data.plot('x', 'y', legend=False, ax=plot, **kwargs)


def plot_place_cells(pcs, plot=None, **kwargs):
    if plot is None:
        plot = plot_new()
        plot.autoscale(enable=True)

    set_defaults(kwargs, {'edgecolor': (0.8, 0.8, 0.8),
                          'facecolor': 'none'})

    for index, row in pcs.iterrows():
        p = patches.Circle([row['x'], row['y']], radius=row['placeradius'], **kwargs)
        plot.add_patch(p)
    return plot


def plot_feeders(data, plot=None, **kwargs):
    set_defaults(kwargs, {'color': 'r',
                          'legend': False})
    data.plot.scatter('x', 'y', ax=plot, **kwargs)
    return plot


def plot_path(data, plot=None, **kwargs):
    set_defaults(kwargs, {'legend': False})
    return data.plot('x', 'y', ax=plot, **kwargs)


def plot_activation_matrix_heatmap(activations, plot=None):
    return (plt if plot is None else plot).imshow(activations, cmap='hot', interpolation='nearest')








