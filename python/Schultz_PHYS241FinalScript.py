"""
PHYS 241 Final Project Script
Author: Matthew Schultz
Description: This script performs a Birch-Murnaghan Equation of State fit for Copper 
and calculates the lowest three wavefunctions for a 1D square potential.
"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Imported functions from my modules
from calculate_quadratic_fit import calculate_quadratic_fit
from equations_of_state import fit_equation_of_state
from annotate_plot import annotate_plot
from generate_matrix import generate_matrix
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors

def main():
    author_name = "Matthew Schultz"
    today = datetime.now().strftime('%Y-%m-%d')
    footer_text = f"Created by {author_name} {today}"
    ev_to_gpa = 160.21766208


    # FIGURE 1: Birch-Murnaghan EOS for Cu
    data_file = "Cu.Fm-3m.GGA-PBE.volumes_energies.dat"

    raw_data = np.loadtxt(data_file).T
    volumes, energies = raw_data[0], raw_data[1]

    quad_coeffs = calculate_quadratic_fit(raw_data)

    num_fit_points = 100
    fit_curve_energies, eos_params = fit_equation_of_state(
        volumes, energies, quad_coeffs,
        equation_of_state='birch-murnaghan',
        number_of_points=num_fit_points
    )

    e0, k0_ev, kp, v0 = eos_params
    k0_gpa = k0_ev * ev_to_gpa

    plt.figure(1, figsize=(8, 6))
    fit_volumes = np.linspace(np.min(volumes), np.max(volumes), num_fit_points)
    plt.plot(fit_volumes, fit_curve_energies, 'k-', label='Fit')
    plt.scatter(volumes, energies, color='blue', label='Data')

    plt.title("Birch-Murnaghan Equation of State for Cu (GGA-PBE)")
    plt.xlabel(r"$V$ ($\mathring{A}^3$/atom)")
    plt.ylabel(r"$E$ (eV/atom)")
    plt.text(0.1, 0.9, "Cu", transform=plt.gca().transAxes, fontsize=12)
    plt.text(0.5, 0.85, "Fm-3m", transform=plt.gca().transAxes, ha='center')

    plt.text(0.5, 0.75, f"$K_0 = {k0_gpa:.1f}$ GPa", transform=plt.gca().transAxes, ha='center')
    plt.text(0.5, 0.65, rf"$V_0 = {v0:.2f}$ $\mathring{{A}}^3$/atom", transform=plt.gca().transAxes, ha='center')

    ann_footer = {
        footer_text: {
            'position': [0.02, 0.02],
            'alignment': ('left', 'bottom'),
            'fontsize': 9
        }
    }
    annotate_plot(ann_footer)

    # Save the figure as required by the rubric
    plt.savefig("Schultz_Cu_EOS.png")

    # FIGURE 2: Square Potential Wavefunctions
    min_x, max_x = -10, 10
    n_dim = 130
    potential_type = 'square'
    potential_param = 2.0

    hamiltonian = generate_matrix(min_x, max_x, n_dim, potential_type, potential_param)

    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(hamiltonian, number_of_eigenvectors=3)

    plt.figure(2, figsize=(8, 6))
    x_grid = np.linspace(min_x, max_x, n_dim)

    colors = ['tab:blue', 'tab:orange', 'tab:green']
    for i in range(3):
        label = rf"$\psi_{i+1}, E_{i+1} = {eigenvalues[i]:.3f}$ a.u."
        plt.plot(x_grid, eigenvectors[i], label=label, color=colors[i])

    plt.axhline(0, color='black', linewidth=0.5)
    plt.title(f"Select Wavefunctions for a Square Potential (N={n_dim})")
    plt.xlabel("x [a.u.]")
    plt.ylabel(r"$\psi_n(x)$ [a.u.]")
    plt.legend()

    annotate_plot(ann_footer)

    # Save the figure as required by the rubric
    plt.savefig("Schultz_Square_Wavefunctions.png")

    plt.show()

if __name__ == "__main__":
    main()