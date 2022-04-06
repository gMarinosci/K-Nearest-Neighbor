import knn_lib as kl
import plotting_lib as pl
import os

path = os.getcwd()
path += '/datasets/microchips.csv'
X, y = kl.get_data(path)
pl.plot_original_data(X, y)
