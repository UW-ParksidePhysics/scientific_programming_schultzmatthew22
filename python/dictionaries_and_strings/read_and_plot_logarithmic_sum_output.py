import matplotlib.pyplot as plt


def parse_sum_output(filename='logarithmic_sum.out'):
    tolerances = []
    errors = []
    maximum_indices = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                if 'epsilon:' in line and 'exact error:' in line:
                    parts = line.split(',')

                    epsilon_val = float(parts[0].split(':')[1].strip())

                    error_val = float(parts[1].split(':')[1].strip())

                    n_val = int(parts[2].split('=')[1].strip())

                    tolerances.append(epsilon_val)
                    errors.append(error_val)
                    maximum_indices.append(n_val)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("run 'python3 logarithmic_sum.py > logarithmic_sum.out' first.")
        return [], [], []

    return tolerances, errors, maximum_indices


def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    if not maximum_indices:
        return

    plt.figure(figsize=(10, 6))

    plt.semilogy(maximum_indices, tolerances, marker='o', label=r'Tolerance ($\epsilon$)')
    plt.semilogy(maximum_indices, errors, marker='s', label=r'Approximation Error ($\Delta$)')

    plt.title('Tolerance and Approximation Error vs Maximum Index (n)')
    plt.xlabel(r'Maximum Index ($n$)')
    plt.ylabel('Value (Logarithmic Scale)')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()

    plt.show()


if __name__ == '__main__':
    tols, errs, max_inds = parse_sum_output('logarithmic_sum.out')
    plot_logarithmic_sum_error(tols, errs, max_inds)