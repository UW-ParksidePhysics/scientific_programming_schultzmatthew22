fahrenheit = 0

print(f"{'Fahrenheit':>5}: | {'Celsius':>7}")
print("-" * 15)

while fahrenheit <= 100:
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:>5} | {celsius:>7.2f}")
    fahrenheit += 10
