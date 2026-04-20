v0 = 10.0
n = 8
gravity_earth = 9.81
gravity_mars = 3.71

time_end_earth = 2 * v0 / gravity_earth
time_end_mars = 2 * v0 / gravity_mars

h_earth = time_end_earth / n
h_mars = time_end_mars / n

print(f"For initial velocity of {v0:.2f} m/s:")
print(f"{'Earth (g = 9.81)':<20} {'Mars (g = 3.71)':<20}")
print(f"{'t (s)':>7} {'y (m)':>10} {'t (s)':>10} {'y (m)':>10}")
print("-" * 50)

print("using a for loop:")
for i in range(n + 1):
    t_e = i * h_earth
    y_e = v0 * t_e - 0.5 * gravity_earth * t_e ** 2

    t_m = i * h_mars
    y_m = v0 * t_m - 0.5 * gravity_mars * t_m ** 2

    print(f"{t_e:7.3f} {y_e:10.3f} {t_m:10.3f} {y_m:10.3f}")

print("\nusing a while loop:")
i = 0

while i <= n + 1e-10:
    t_e = i * h_earth
    y_e = v0 * t_e - 0.5 * gravity_earth * t_e ** 2

    t_m = i * h_mars
    y_m = v0 * t_m - 0.5 * gravity_mars * t_m ** 2

    print(f"{t_e:7.3f} {y_e:10.3f} {t_m:10.3f} {y_m:10.3f}")
    i += 1