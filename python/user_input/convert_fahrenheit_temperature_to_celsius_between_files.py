def convert_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


if __name__ == '__main__':
    infile = 'temp_data_multi.txt'
    outfile = 'temp_conversions.txt'

    fahrenheit_list = []

    try:
        with open(infile, 'r') as f:
            lines = f.readlines()

            for line in lines[3:]:
                if line.strip():
                    words = line.split()
                    fahrenheit_list.append(float(words[2]))

        celsius_list = [convert_f_to_c(f) for f in fahrenheit_list]

        with open(outfile, 'w') as f:
            f.write(f"{'Fahrenheit':>10} | {'Celsius':>10}\n")
            f.write("-" * 25 + "\n")

            for f_val, c_val in zip(fahrenheit_list, celsius_list):
                f.write(f"{f_val:10.1f} | {c_val:10.2f}\n")

        print(f"Successfully processed {len(fahrenheit_list)} temperatures.")
        print(f"Results written to: {outfile}")

    except FileNotFoundError:
        print(f"Error: Could not find '{infile}'.")
    except (IndexError, ValueError) as e:
        print(f"Error processing file content: {e}")