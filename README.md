import math

# Starting position
position = [0, 0]

# Commands: list of vector moves (x, y)
commands = [
    [4, 0],    # 4 steps right
    [0, 2],    # 2 steps up
    [-1, 0],   # 1 step left
    [0, -3]    # 3 steps down
]

# Apply all vector movements
for move in commands:
    position[0] += move[0]
    position[1] += move[1]

# Final Position
print("Final Position Vector:", position)

# Total Displacement (Euclidean Norm)
displacement = math.sqrt(position[0]**2 + position[1]**2)
print("Total Displacement (Norm):", round(displacement, 2))

# Unit vector (Direction)
if displacement != 0:
    unit_vector = [
        round(position[0] / displacement, 3),
        round(position[1] / displacement, 3)
    ]
else:
    unit_vector = [0, 0]

print("Unit Direction Vector:", unit_vector)
