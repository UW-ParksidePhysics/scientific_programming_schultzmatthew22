fahrenheit = 0

print(f"{'Fahrenheit':>5} | {'Actual Celsius':>8} | {'Approximate Celsius':>8}")
print("-" * 28)

while fahrenheit <= 100:
    celsius = (fahrenheit - 32) * 5 / 9
    approximate_celsius = (fahrenheit - 30) / 2

    print(f"{fahrenheit:5d} | {celsius:6.2f} | {approximate_celsius:6.2f}")

    fahrenheit += 10