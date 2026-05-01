def convert_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


if __name__ == '__main__':
    filename = 'temp_data.txt'

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            fourth_line = lines[3]

            words = fourth_line.split()

            f_temp = float(words[2])

        c_temp = convert_f_to_c(f_temp)
        print(f"{f_temp} degrees Fahrenheit is {c_temp:.2f} degrees Celsius.")

    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'. Make sure it is in the same directory as this script.")
    except IndexError:
        print("Error: The file does not have enough lines or words. Check your temp_data.txt format.")