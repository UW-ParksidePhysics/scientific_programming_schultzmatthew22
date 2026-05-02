import matplotlib.pyplot as plt
import numpy as np


def parse_viscosity_data(filename='viscosity_of_gases.dat'):
    viscosity_data = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            parts = line.split()
            if len(parts) < 4:
                continue

            mu_0 = float(parts[-1])
            T_0 = float(parts[-2])
            C = float(parts[-3])
            name = " ".join(parts[:-3])

            viscosity_data[name] = {
                'viscosity': C,
                'reference_temperature': T_0,
                'reference_viscosity': mu_0
            }

    return viscosity_data


def calculate_viscosity(temperature, gas, viscosity_data):

    data = viscosity_data[gas]
    C = data['viscosity']
    T_0 = data['reference_temperature']
    mu_0 = data['reference_viscosity']

    mu = mu_0 * ((T_0 + C) / (temperature + C)) * (temperature / T_0) ** 1.5
    return mu


def plot_viscosities():
    data_dict = parse_viscosity_data('viscosity_of_gases.dat')

    T_values = np.linspace(223, 373, 100)

    target_gases = ['air', 'carbon dioxide', 'hydrogen']

    plt.figure(figsize=(10, 6))

    for gas in target_gases:
        if gas in data_dict:
            mu_values = [calculate_viscosity(T, gas, data_dict) for T in T_values]
            plt.plot(T_values, mu_values, label=gas.capitalize())

    plt.title('Gas Viscosity vs. Temperature (Sutherland\'s Law)')
    plt.xlabel('Temperature (K)')
    plt.ylabel(r'Viscosity $\mu$ ($10^{-6}$ Pa$\cdot$s)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    plt.show()


if __name__ == '__main__':
    plot_viscosities()