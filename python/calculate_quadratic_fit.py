import numpy as np
from numpy.polynomial import Polynomial


def calculate_quadratic_fit(data):

    if data.shape[0] != 2 or data.shape[1] < 3:
        raise IndexError("Quadratic fit requires (2, M) array with M >= 3.")

    p = Polynomial.fit(data[0], data[1], 2)
    return p.convert().coef


if __name__ == "__main__":
    x_test = np.linspace(-1, 1)
    data_test = np.array([x_test, x_test ** 2])
    coeffs = calculate_quadratic_fit(data_test)
    print(f"Quadratic Coefficients (c0, c1, c2): {coeffs}")
#