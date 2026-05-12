import numpy as np
import os


def read_two_columns_text(filename):
    if not os.path.exists(filename):
        raise OSError(f"The file '{filename}' was not found.")

    data = np.loadtxt(filename).T
    return data


if __name__ == "__main__":
    try:
        data = read_two_columns_text('volumes_energies.dat')
        print(f'{data=}, shape={data.shape}')
    except OSError as e:
        print(f"Error: {e}")
#