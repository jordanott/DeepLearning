import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import warnings
from matplotlib.colors import ListedColormap

warnings.filterwarnings('ignore')

np.random.seed(0)


def plot_decision_boundary(df, theta):
    xx, yy = np.meshgrid(np.arange(-.2, 1.2, .02),np.arange(-.2, 1.2, .02))
    Z = np.dot(np.c_[xx.ravel(), yy.ravel()], theta) > 0
    Z = Z.reshape(xx.shape)

    plt.pcolormesh(xx, yy, Z,cmap=ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF']))
    plt.scatter(df['x1'],df['x2'],c=df['y'],cmap=ListedColormap(['#FF0000', '#00FF00', '#0000FF']))
    plt.show()