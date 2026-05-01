import numpy as np
import matplotlib.pyplot as plt


def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x ** 2)


if __name__ == '__main__':
    start, stop, n = -4, 4, 101

    x_values = np.linspace(start, stop, n)
    y_values = gaussian(x_values)

    plt.plot(x_values, y_values, 'b-', label='Gaussian Distribution')

    plt.xlabel('x Position')
    plt.ylabel('Gaussian Value g(x)')

    plt.grid(True)
    plt.legend()

    print("Close the plot window to finish the program.")
    plt.show()