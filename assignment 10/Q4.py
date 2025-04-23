import numpy as np

# Step 1: Take input N (>= 10)
N = 10  # You can change this value as needed

# Step 2: Generate N random 2D points in Cartesian coordinates
# Random points in range (-10, 10) for both x and y
cartesian_points = np.random.uniform(-10, 10, size=(N, 2))

# Step 3: Convert to polar coordinates
# r = sqrt(x^2 + y^2), theta = arctangent(y / x)
x = cartesian_points[:, 0]
y = cartesian_points[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)  # angle in radians

polar_points = np.column_stack((r, theta))

# Step 4: Print results
print("Cartesian Coordinates:\n", cartesian_points)
print("\nPolar Coordinates (r, theta in radians):\n", polar_points)


