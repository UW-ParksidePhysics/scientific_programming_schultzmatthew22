v0 = 10.0
n = 10
g = 9.81

t_end = 2 * v0 / g
h = t_end / n

times = []
positions = []

for i in range(n + 1):
    t = i * h
    y = v0 * t - 0.5 * g * t**2
    times.append(t)
    positions.append(y)

print(f"{'t (s)':>8} | {'y (m)':>8}")
print("-" * 20)

for t, y in zip(times, positions):
    print(f"{t:8.3f} | {y:8.3f}")