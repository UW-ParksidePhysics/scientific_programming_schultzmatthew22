import numpy as np


def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):

    m, n = square_matrix.shape
    if m != n:
        raise IndexError("Input matrix must be square.")
    if not (1 <= number_of_eigenvectors <= m):
        raise IndexError(f"number_of_eigenvectors must be between 1 and {m}.")

    evals, evecs = np.linalg.eig(square_matrix)

    idx = np.argsort(evals)
    sorted_evals = evals[idx[:number_of_eigenvectors]]

    sorted_evecs = evecs[:, idx[:number_of_eigenvectors]].T

    return sorted_evals, sorted_evecs


if __name__ == "__main__":
    mat = np.array([[2, -1], [-1, 2]])
    vals, vecs = calculate_lowest_eigenvectors(mat, 2)
    print(f"Lowest Eigenvalues: {vals}")
    print(f"Corresponding Eigenvectors:\n{vecs}")
