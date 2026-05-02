# Note: I duplicated the first file that had all the notes and stuff and put that on a second monitor while I worked on this one. It was too jarring for me to scroll up and down with so I put my completed work on this file. If you want all the notes and stuff from the original document please let me know so I can fix it right away

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

M_SUN = 4.83

def star_colormap(star_b_minus_v_values):
    num_points = 256
    color_values = np.ones((num_points, 4))
    color_values[:, 0] = np.clip(np.linspace(0.4, 1.2, num_points), 0, 1)
    color_values[:, 1] = np.clip(np.linspace(0.4, 1.1, num_points), 0, 1)
    color_values[:, 2] = np.clip(np.linspace(1.2, 0.4, num_points), 0, 1)
    new_colormap = ListedColormap(color_values)
    scaled_bv = (star_b_minus_v_values - np.amin(star_b_minus_v_values)) / \
                (np.amax(star_b_minus_v_values) - np.amin(star_b_minus_v_values))
    return scaled_bv, new_colormap

def main():
    with open('hipparcos_data.txt', 'r') as f:
        star_dict = {
            row[0]: {'plx': float(row[1]), 'v': float(row[2]), 'bv': float(row[3])}
            for line in f if (row := line.split()) and float(row[1]) > 0
        }

    bv_indices = np.array([s['bv'] for s in star_dict.values()])
    v_mags = np.array([s['v'] for s in star_dict.values()])
    plx = np.array([s['plx'] for s in star_dict.values()])

    dist_pc = 1000.0 / plx
    abs_mags = v_mags - 5 * np.log10(dist_pc) + 5

    plot_mags = -abs_mags

    special_stars = {
        "Sun": (0.65, 4.83), "Sirius": (0.00, 1.42), "Canopus": (0.15, -5.53),
        "Rigil Kentaurus": (0.71, 4.34), "Arcturus": (1.23, -0.31), "Vega": (0.00, 0.58)
    }

    plt.style.use('dark_background')
    fig, ax1 = plt.subplots(figsize=(10, 12))

    scaled_bv, hr_cmap = star_colormap(bv_indices)
    ax1.scatter(bv_indices, plot_mags, s=1, c=scaled_bv, cmap=hr_cmap, alpha=0.5)

    for name, (bv, mag) in special_stars.items():
        ax1.scatter(bv, -mag, color='white', edgecolors='red', s=60, zorder=5)
        ax1.text(bv + 0.05, -mag, name, color='white', fontsize=9, weight='bold')

    ax1.set_xlim(-0.5, 2.5)
    ax1.set_ylim(-15, 10)
    ax1.set_xlabel("Color Index (B-V)")
    ax1.set_ylabel("Absolute Magnitude (Reversed Scale)")

    ax2 = ax1.twinx()
    ax2.set_ylim(ax1.get_ylim())
    y_ticks = np.array([-10, -5, 0, 5, 10])
    ax2.set_yticks(y_ticks)
    ax2.set_yticklabels([f"$10^{{{round((M_SUN - (-y))/2.5, 1)}}}$" for y in y_ticks])
    ax2.set_ylabel("Luminosity ($L/L_{\odot}$)")

    ax3 = ax1.twiny()
    ax3.set_xlim(ax1.get_xlim())
    ax3.set_xticks([-0.3, 0.0, 0.3, 0.6, 0.8, 1.4, 2.0])
    ax3.set_xticklabels(["O", "B", "A", "F", "G", "K", "M"])
    ax3.set_xlabel("Spectral Class")

    ax1.text(0.02, 0.02, 'Created by Matthew', transform=ax1.transAxes, color='white', fontsize=12)
    plt.title("Hertzsprung-Russell Diagram (Hipparcos Data)", pad=30)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()