import numpy as np
import math


def gaussian(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x ** 2)


if __name__ == '__main__':
    start, stop, n = -4, 4, 41

    x_values = np.zeros(n)
    y_values = np.zeros(n)

    step = (stop - start) / (n - 1)

    for i in range(n):
        x = start + i * step
        x_values[i] = x
        y_values[i] = gaussian(x)

    print("Index |   x_values   |   y_values")
    print("-" * 37)
    for i in range(5):
        print(f"{i:5} | {x_values[i]:12.4f} | {y_values[i]:12.4f}")