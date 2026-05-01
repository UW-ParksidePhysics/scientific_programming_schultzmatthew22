import sys
import numpy as np
import matplotlib.pyplot as plt


def f(x, y0, theta, v0, g=9.81):
    theta_rad = np.radians(theta)

    term1 = x * np.tan(theta_rad)
    term2 = (g * x ** 2) / (2 * v0 ** 2 * np.cos(theta_rad) ** 2)
    return term1 - term2 + y0


if __name__ == '__main__':
    try:
        y0 = float(sys.argv[1])
        theta = float(sys.argv[2])
        v0 = float(sys.argv[3])

        x_max = (v0 ** 2 / 9.81) * np.sin(np.radians(2 * theta)) + (v0 * y0) + 10.0

        x_vals = np.linspace(0, x_max, 1000)
        y_vals = f(x_vals, y0, theta, v0)

        indices = np.where(y_vals >= 0)
        x_plot = x_vals[indices]
        y_plot = y_vals[indices]

        plt.plot(x_plot, y_plot, 'r-', label=f'v0={v0}, theta={theta}°')
        plt.title(r'Trajectory of a Ball ($y \geq 0$)')
        plt.xlabel('Horizontal Distance (x)')
        plt.ylabel('Vertical Height (y)')
        plt.axhline(0, color='black', lw=1)  # Ground line
        plt.grid(True)
        plt.legend()
        plt.show()

    except (IndexError, ValueError):
        print("Usage: python plot_trajectory.py <y0> <theta> <v0>")