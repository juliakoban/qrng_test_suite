import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (8, 6))
plt.rcParams['font.family'] = 'Times New Roman'  # Czcionka Times New Roman
plt.rcParams['font.size'] = 15  # Rozmiar czcionki
plt.rcParams['axes.labelsize'] = 15 # Rozmiar etykiet osi
plt.rcParams['xtick.labelsize'] = 15  # Rozmiar etykiet na osi X
plt.rcParams['ytick.labelsize'] = 15  # Rozmiar etykiet na osi Y


# Example data (x = number of bits, y = time in seconds)
x = [5, 10, 15, 20, 25, 26, 27]  # Number of bits
y = [2.23, 2.59,2.76, 6.90, 39.61, 75.01, 1219.60]  # Time in seconds

# Create a plot
plt.scatter(x, y, marker='o', color='black')

# Label the axes
plt.xlabel('Długość wzorca n [bit]', fontsize=15, fontweight='bold')
plt.ylabel('Czas wykonania testu [s]', fontsize=15, fontweight='bold')

# Title of the plot
plt.title('Czas testu wyszukiwania n-bitowych wzorców w sekwencji o długości 10 milionów bitów', fontsize = 15, fontweight = 'bold')

# plt.xscale('log')
# Display grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Show the plot
plt.show()
