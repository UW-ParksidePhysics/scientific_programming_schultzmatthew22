import numpy as np
import matplotlib.pyplot as plt

n = 5
h_step = 1 / (n + 1)
scaling_factor = 1 / (2 * (h_step**2))

main_diag = np.diagflat(2 * np.ones(n))
off_diag_low = np.diagflat(-1 * np.ones(n - 1), k=-1)
off_diag_high = np.diagflat(-1 * np.ones(n - 1), k=1)

H = scaling_factor * (main_diag + off_diag_low + off_diag_high)

eigenvalues, eigenvectors = np.linalg.eig(H)

idx = eigenvalues.argsort()
eigenvectors = eigenvectors[:, idx]

fifth_eigenvector = eigenvectors[:, 4]

x_values = np.linspace(1/6, 5/6, 5)
x_continuous = np.linspace(0, 1, 100)
y_continuous = np.sqrt(2) * np.sin(np.pi * x_continuous)

plt.figure(figsize=(8, 5))
plt.plot(x_continuous, y_continuous, label=r'$\sqrt{2}\sin(\pi x)$', color='blue')
plt.scatter(x_values, fifth_eigenvector, color='red', label='5th Eigenvector')
plt.grid(True)
plt.show()
