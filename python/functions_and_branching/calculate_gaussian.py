import math

def gaussian(position, mean=0, standard_deviation=1):
    x = position
    mu = mean
    sigma = standard_deviation

    coefficient = 1 / (math.sqrt(2 * math.pi) * sigma)
    exponent = -0.5 * ((x - mu) / sigma) ** 2

    return coefficient * math.exp(exponent)

m = 0
s = 1
n = 11

start = m - 5 * s
stop = m + 5 * s
step = (stop - start) / (n - 1)

print(f"{'x':>10} | {'f(x)':>10}")
print("-" * 25)

for i in range(n):
    x_val = start + i * step
    y_val = gaussian(x_val, mean=m, standard_deviation=s)
    print(f"{x_val:10.2f} | {y_val:10.5f}")