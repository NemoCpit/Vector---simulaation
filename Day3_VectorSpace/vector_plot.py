import matplotlib.pyplot as plt
import numpy as np

# Define vectors
v1 = np.array([2, 1])
v2 = np.array([1, 3])
result = 2 * v1 + 3 * v2  # Linear combination result

# Setup the plot
plt.figure(figsize=(6, 6))
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

# Plot vectors
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='green', label='v2')
plt.quiver(0, 0, result[0], result[1], angles='xy', scale_units='xy', scale=1, color='red', label='2v1 + 3v2')

# Formatting
plt.xlim(0, 10)
plt.ylim(0, 12)
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Linear Combination: 2*v1 + 3*v2")
plt.show()
