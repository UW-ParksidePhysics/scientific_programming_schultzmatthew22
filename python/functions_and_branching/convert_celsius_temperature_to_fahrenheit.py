def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    return (5 / 9) * (fahrenheit_temperature - 32)

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    return (9 / 5) * celsius_temperature + 32

test_temps = [0, 21, 100]

print(f"{'Input Celsius':<15} | {'Resulting Celsius':<20}")
print("-" * 40)
for c_in in test_temps:
    f_temp = convert_celsius_temperature_to_fahrenheit(c_in)
    c_out = convert_fahrenheit_temperature_to_celsius(f_temp)

    print(f"{c_in:<15} | {c_out:<20.1f}")