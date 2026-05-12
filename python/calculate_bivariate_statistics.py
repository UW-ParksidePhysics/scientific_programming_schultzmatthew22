import numpy as np
from scipy import stats


def calculate_bivariate_statistics(data):
    if data.shape[0] != 2 or data.shape[1] < 2:
        raise IndexError("Data must have shape (2, M) with at least 2 columns.")

    x, y = data[0], data[1]
    desc = stats.describe(y)

    mean_y = desc.mean
    std_y = np.sqrt(desc.variance)
    min_x, max_x = np.min(x), np.max(x)
    min_y, max_y = np.min(y), np.max(y)

    return np.array([mean_y, std_y, min_x, max_x, min_y, max_y])


if __name__ == "__main__":
    x_test = np.linspace(-10, 10, 21)
    data_test = np.array([x_test, x_test ** 2])
    stats_out = calculate_bivariate_statistics(data_test)
    print(f"Bivariate Statistics (Mean Y, Std Y, Min X, Max X, Min Y, Max Y):\n{stats_out}")
#