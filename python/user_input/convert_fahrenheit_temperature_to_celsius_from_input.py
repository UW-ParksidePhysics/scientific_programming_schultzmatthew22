def convert_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


if __name__ == '__main__':
    user_input = input("Enter temperature in Fahrenheit: ")
    f_temp = float(user_input)

    c_temp = convert_f_to_c(f_temp)

    print(f"{f_temp} degrees Fahrenheit is {c_temp:.2f} degrees Celsius.")
