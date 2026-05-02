#### RENAME THIS FILE
# Rename `project.py` to `(your_project_short_name).py`
# Example: `orbit_simulation.py`, `wave_packet.py`, `two_body_problem.py`

# -----------------------------------------------------------------------------
# PROJECT FILE STRUCTURE (CONTEMPORARY PYTHON BEST PRACTICES)
# -----------------------------------------------------------------------------
# The goal is clarity, testability, and “import safety” (importing your module
# should NOT start the simulation or pop up plots).
#
# Recommended top-to-bottom order:
# 1) Module docstring (100–200 words): what the project does, key assumptions,
#    inputs/outputs, and how to run it.
# 2) Imports (grouped per PEP 8).
# 3) Module-level constants (only if truly global and stable).
# 4) Function definitions (each with a PEP 257-compliant docstring).
# 5) main() function: the single clear entry point for running the program.
# 6) Script guard: if __name__ == "__main__": main()
#
# References:
# - PEP 8 (imports and general style): https://peps.python.org/pep-0008/  (see “Imports”)
# - SciPy physical constants (use inside functions when appropriate):
#   https://docs.scipy.org/doc/scipy/reference/constants.html
#
# -----------------------------------------------------------------------------
# IMPORTS: ORDER + PRACTICES (PEP 8)
# -----------------------------------------------------------------------------
# Put imports at the top, after the module docstring, before constants.
# Group imports in THIS order, separated by blank lines:
#   1) Standard library imports (e.g., math, pathlib, dataclasses)
#   2) Third-party imports (e.g., numpy, scipy, matplotlib, plotly)
#   3) Local/project imports (your own modules in this repo/package)
#
# Examples:
#   # 1) Standard library
#   from __future__ import annotations
#   from dataclasses import dataclass
#   from pathlib import Path
#
#   # 2) Third-party
#   import numpy as np
#   from scipy import constants as scipy_constants
#
#   # 3) Local imports (if your project is a package)
#   # from .helpers import integrate
#
# Avoid:
# - wildcard imports: `from module import *`
# - hiding heavy work at import time (reading big files / launching plots)
#
# -----------------------------------------------------------------------------
# SIMULATION / VISUALIZATION FUNCTIONS (FUNCTIONAL STYLE)
# -----------------------------------------------------------------------------
# Keep “work” inside functions. This makes your code testable and reusable.
#
# Typical breakdown:
# - read_data(...): load/validate input data
# - compute_derived_parameters(...): compute values that depend on inputs
# - simulate(...): compute arrays / time series (no plotting)
# - build_figure(...): create a plot/animation object (no file I/O)
# - save_outputs(...): optional, write files if required
#
# Each function must have:
# - clear, full-word parameter names (PEP 8: lower_case_with_underscores)
# - units in comments or docstrings (meters, seconds, kg, etc.)
# - a docstring describing: parameters, returns, and assumptions
#
# -----------------------------------------------------------------------------
# SciPy CONSTANTS: WHERE TO USE THEM
# -----------------------------------------------------------------------------
# Prefer importing SciPy constants inside the function that uses them, so the
# dependency is obvious and to keep module import fast/lightweight.
#
# Example pattern (inside a function):
#   from scipy import constants as scipy_constants
#   speed_of_light = scipy_constants.c
#
# Docs: https://docs.scipy.org/doc/scipy/reference/constants.html
#
# -----------------------------------------------------------------------------
# main(): THE STANDARD ENTRY POINT
# -----------------------------------------------------------------------------
# It is now standard practice to put the “run the program” logic in a main()
# function and call it under the script guard. This prevents side effects when
# importing your module.
#
# Skeleton:
#   def main() -> None:
#       """Run the simulation and display/save results."""
#       # 1) Define simulation parameters (with units)
#       # 2) Compute derived parameters
#       # 3) Call read_data / simulate / build_figure
#       # 4) Show or save outputs
#
#   if __name__ == "__main__":
#       main()
#
# -----------------------------------------------------------------------------
# PRIMARY SIMULATION FUNCTION STRUCTURE (SUGGESTED)
# -----------------------------------------------------------------------------
# Inside your primary simulation function (often called by main()):
# 1) Parameters (named clearly, units documented)
# 2) Derived parameters (computed from inputs)
# 3) Call helpers for:
#    - data read-in / validation
#    - simulation computation
#    - visualization creation
# 4) Return results (arrays, figure objects) instead of printing everything
#
# Keep plotting separate from physics/math wherever practical.

<<<<<<< Updated upstream:python/project/project.py
import turtle

import matplotlib.pyplot as plt

# Constants
R_KM = {
    "Mercury": 2440,
    "Venus": 6052,
    "Earth": 6371,
    "Mars": 3390,
    "Jupiter": 69911,
    "Saturn": 58232,
    "Uranus": 25362,
    "Neptune": 24622,
}

DESIRED_MAX_DIAMETER_MM = 220
K = DESIRED_MAX_DIAMETER_MM / (2 * R_KM["Jupiter"])


def generate_data_matrix():
    data_matrix = []
    current_x = -550.0
    y_pos = 0.0
    buffer = 45

    planet_names = list(R_KM.keys())

    for i, name in enumerate(planet_names):
        r_km = R_KM[name]
        r_scaled_mm = r_km * K

        if i == 0:
            x_pos = current_x + r_scaled_mm
        else:
            prev_r = data_matrix[i - 1][1]
            prev_x = data_matrix[i - 1][2]

            min_center_dist = r_scaled_mm + prev_r + buffer
            x_pos = prev_x + min_center_dist

        data_matrix.append([name, r_scaled_mm, x_pos, y_pos, r_km])

    return data_matrix


def show_comparison_graphs(matrix):
    names = [row[0] for row in matrix]
    r_km = [row[4] for row in matrix]
    r_mm = [row[1] for row in matrix]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.bar(names, r_km, color='#1565C0')
    ax1.set_title("Radius in km")

    ax2.bar(names, r_mm, color='#C62828')
    ax2.set_title("Radius in mm (Scaled)")

    plt.tight_layout()
    plt.show(block=False)
    plt.pause(0.1)


def draw_turtle_stencil(matrix):
    screen = turtle.Screen()
    screen.setup(width=1300, height=700)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    colors = [
        "#9E9E9E", "#E3BB76", "#2E7D32", "#D32F2F",
        "#EF6C00", "#F4E0AF", "#4DD0E1", "#1565C0"
    ]

    for i, row in enumerate(matrix):
        name, r_mm, x, y, r_km = row

        t.goto(x, y - r_mm)
        t.pendown()
        t.color(colors[i])
        t.begin_fill()
        t.circle(r_mm)
        t.end_fill()
        t.penup()

        label_y = y + r_mm + (20 if i % 2 == 0 else 80)
        t.goto(x, label_y)
        t.color("black")
        t.pendown()
        t.goto(x, y + r_mm + 2)
        t.penup()
        t.goto(x, label_y)

        # Wrapped string variables to adhere to line-length limits
        label_text = f"{name}\nReal: {int(r_km):,} km\nStencil: {r_mm:.2f} mm"
        t.write(
            label_text,
            align="center",
            font=("Arial", 8, "bold")
        )

    t.hideturtle()
    print("Stencil Complete. You can close the Plot and the Turtle window.")
    turtle.done()


if __name__ == "__main__":
    matrix = generate_data_matrix()

    turtle.getscreen()
    show_comparison_graphs(matrix)
    draw_turtle_stencil(matrix)
=======

def plot_stencil():
    return


def main() -> None:
    """Run the simulation and display/save results."""
    # 1) Define simulation parameters (with units)
    # 2) Compute derived parameters
    # 3) Call read_data / simulate / build_figure
    plot_stencil()
    # 4) Show or save outputs

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes:python/project/planet_stencils.py
