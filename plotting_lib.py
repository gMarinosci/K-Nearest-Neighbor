import matplotlib.pyplot as plt


def plot_original_data(X, y):
    plt.figure(figsize=(5, 5))
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
    plt.title('Original data')
    plt.show()
    pass
