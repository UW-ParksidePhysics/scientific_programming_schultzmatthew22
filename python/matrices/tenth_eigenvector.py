import numpy as np
import matplotlib.pyplot as plt

matrix_dimension = 10

n = matrix_dimension
h = 1 / (n + 1)
scaling = 1 / (2 * (h**2))

matrix = scaling * (np.diagflat(2 * np.ones(n)) +
                    np.diagflat(-1 * np.ones(n - 1), 1) +
                    np.diagflat(-1 * np.ones(n - 1), -1))

val, vec = np.linalg.eig(matrix)

tenth_vec = vec[:, n - 1]

x_vals = np.linspace(1/(n+1), n/(n+1), n)
x_cont = np.linspace(0, 1, 100)
y_cont = np.sqrt(2) * np.sin(np.pi * x_cont)

plt.plot(x_cont, y_cont)
plt.scatter(x_vals, tenth_vec)
plt.show()
