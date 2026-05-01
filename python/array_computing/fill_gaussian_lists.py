import math


def gaussian(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x ** 2)


if __name__ == '__main__':
    start, stop, n = -4, 4, 41

    step = (stop - start) / (n - 1)

    positions = [start + i * step for i in range(n)]
    gaussian_values = [gaussian(x) for x in positions]

    print(f"{'Position (x)':>15} | {'g(x)':>10}")
    print("-" * 30)
    for pos, val in zip(positions[:5], gaussian_values[:5]):
        print(f"{pos:15.2f} | {val:10.4f}")
    print("...")