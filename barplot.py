import matplotlib.pyplot as plt
import numpy as np


def plot_bar_x(x_axis, y_axis, x_label, y_label, title):
    # this is for plotting purpose
    index = np.arange(len(x_axis))
    plt.bar(index, y_axis)
    plt.xlabel(x_label, fontsize=5)
    plt.ylabel(y_label, fontsize=5)
    plt.xticks(index, x_axis, fontsize=5, rotation=30)
    plt.title(title)
    plt.show()
