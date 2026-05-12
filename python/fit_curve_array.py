import numpy as np
from numpy.polynomial import Polynomial


def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points=100):

    if maximum_x < minimum_x:
        raise ArithmeticError("maximum_x must be >= minimum_x.")
    if number_of_points <= 2:
        raise IndexError("Number of points must be greater than 2.")

    x_fit = np.linspace(minimum_x, maximum_x, number_of_points)
    p = Polynomial(quadratic_coefficients)
    y_fit = p(x_fit)

    return np.array([x_fit, y_fit])


if __name__ == "__main__":
    curve = fit_curve_array([0, 0, 1], -2, 2)
    print(f"Fit Curve Sample (last 3 points):\n{curve[:, -3:]}")
