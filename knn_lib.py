import numpy as np
import pandas as pd
import pandas as pn
import csv


def get_data(file_path):
    X = []
    y = []

    with open(file_path) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            X.append([float(row[0]), float(row[1])])
            y.append(int(row[2]))
    return np.array(X), np.array(y)


def euclidean_distance(data1, data2, length):
    dist = 0

    for x in range(length):
        dist += np.square(data1[x] - data2[x])

    return np.sqrt(dist)
