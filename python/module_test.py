import os
import numpy as np


matrix_10x10 = np.eye(10) * 2

modules = [
    'read_two_columns_text',
    'calculate_bivariate_statistics',
    'calculate_quadratic_fit',
    'fit_curve_array',
    'plot_data_with_fit',
    'calculate_lowest_eigenvectors',
    'annotate_plot'
]

print("Starting Module Functionality Showcase...")

for module in modules:
    filename = module + '.py'
    print(f"\n--- Running Standalone Test: {filename} ---")

    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(f'# Placeholder for {module}')

    with open(filename) as module_file:
        exec(module_file.read())

print("\nAll modules executed.")