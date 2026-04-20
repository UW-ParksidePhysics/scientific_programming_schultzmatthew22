v0 = 5.0
g = 9.81
n = 11
t_end = 1.0

times = [i * (t_end/(n-1)) for i in range(n)]
positions = [v0 * t - 0.5 * g * t ** 2 for t in times]

times_positions = [times, positions]

print(f"{'t (s)':>10} {'y (m)':>10}")
print("-" * 22)

for i in range(len(times_positions[0])):
    t = times_positions[0][i]
    y = times_positions[1][i]
    print(f"{t:10.2f} {y:10.2f}")

print("\n")

time_positions = []
for t, y in zip(times, positions):
    time_positions.append([t, y])

print(f"{'t (s)':>10} {'y (m)':>10}")
print("-" * 22)

for t, y in time_positions:
    print(f"{t:10.2f} {y:10.2f}")