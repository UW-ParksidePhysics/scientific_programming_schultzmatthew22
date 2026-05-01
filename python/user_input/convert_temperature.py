import sys

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def test_conversion():
    tol = 1e-10
    success = True

    f_val, c_val, k_val = 100.0, 20.0, 300.0

    test1 = abs(celsius_to_fahrenheit(fahrenheit_to_celsius(f_val)) - f_val) < tol
    test2 = abs(kelvin_to_celsius(celsius_to_kelvin(c_val)) - c_val) < tol
    test3 = abs(kelvin_to_fahrenheit(fahrenheit_to_kelvin(f_val)) - f_val) < tol

    if not (test1 and test2 and test3):
        success = False

    assert success, "Verification failed: One or more conversions are inaccurate."
    print("All tests passed.")

def user_interface():
    try:
        value = float(sys.argv[1])
        scale = sys.argv[2].upper()

        if scale == 'C':
            f = celsius_to_fahrenheit(value)
            k = celsius_to_kelvin(value)
            print(f"{f:.1f} F")
            print(f"{k:.1f} K")
        elif scale == 'F':
            c = fahrenheit_to_celsius(value)
            k = fahrenheit_to_kelvin(value)
            print(f"{c:.1f} C")
            print(f"{k:.1f} K")
        elif scale == 'K':
            c = kelvin_to_celsius(value)
            f = kelvin_to_fahrenheit(value)
            print(f"{c:.1f} C")
            print(f"{f:.1f} F")
        else:
            print("Unknown scale. Use C, F, or K.")

    except (IndexError, ValueError):
        print("Usage: python convert_temperature.py <value> <scale>")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'verify':
        test_conversion()
    else:
        user_interface()