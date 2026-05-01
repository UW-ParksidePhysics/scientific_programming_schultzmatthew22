import numpy as np


def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x ** 2)


if __name__ == '__main__':
    start, stop, n = -4, 4, 41

    x_values = np.linspace(start, stop, n)

    y_values = gaussian(x_values)

    print(f"{'x_values':>12} | {'y_values':>12}")
    print("-" * 27)
    for x, y in zip(x_values[:5], y_values[:5]):
        print(f"{x:12.4f} | {y:12.4f}")