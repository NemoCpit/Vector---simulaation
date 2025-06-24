import numpy as np

# Define two vectors
v1 = np.array([2, 1])
v2 = np.array([1, 3])

# Define scalars (weights)
alpha = 3
beta = -2

# Linear combination: v = α * v1 + β * v2
v = alpha * v1 + beta * v2

# Output
print("v1 =", v1)
print("v2 =", v2)
print(f"Linear Combination: {alpha} * v1 + {beta} * v2 = {v}")
