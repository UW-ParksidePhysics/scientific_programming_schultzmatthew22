import sys


def convert_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == '__main__':
    try:
        f_temp = float(sys.argv[1])

        c_temp = convert_f_to_c(f_temp)

        print(f"{f_temp} degrees Fahrenheit is {c_temp:.2f} degrees Celsius.")

    except IndexError:
        print("Error: The Fahrenheit temperature is missing on the command line.")

    except ValueError:
        print("Error: The provided argument must be a number.")