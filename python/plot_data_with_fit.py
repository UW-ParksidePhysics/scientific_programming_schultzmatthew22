import matplotlib.pyplot as plt
import numpy as np


def plot_data_with_fit(data, fit_curve, data_format='o', fit_format=''):
    if data.shape[0] != 2 or fit_curve.shape[0] != 2:
        raise IndexError("Both input arrays must have 2 rows.")

    p1 = plt.plot(data[0], data[1], data_format)
    p2 = plt.plot(fit_curve[0], fit_curve[1], fit_format)
    return p1 + p2


if __name__ == "__main__":
    data = np.array([[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
    fit = np.array([np.linspace(-2, 2), np.linspace(-2, 2) ** 2])
    plot_data_with_fit(data, fit, data_format='x', fit_format='--')
    plt.show()
