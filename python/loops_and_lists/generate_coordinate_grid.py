a = 1
b = 2
n = 20

h = (b - a) / n

x_for_loop = []
for i in range(n + 1):
    xi = round(a + i * h, 10)
    x_for_loop.append(xi)

x_list_comp = [round(a + i * h, 10) for i in range(n + 1)]

print(f"For x in [{a}, {b}] with {n} intervals, the interval length is h = {h:.4f}, and")

print("Using a for loop:")
print(f"x = {x_for_loop}")
print("Using list comprehension:")
print(f"x = {x_list_comp}")