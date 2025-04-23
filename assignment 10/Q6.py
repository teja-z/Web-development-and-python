import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**3 - x - 2

# Step 1: Find a valid interval [a, b] where f(a) * f(b) < 0
def find_initial_interval():
    for _ in range(1000):  # Try 1000 random pairs
        a = np.random.uniform(-10, 10)
        b = np.random.uniform(-10, 10)
        if f(a) * f(b) < 0:
            return min(a, b), max(a, b)
    raise ValueError("Could not find valid initial interval.")

# Step 2: Bisection Method
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    steps = []
    for _ in range(max_iter):
        c = (a + b) / 2
        steps.append([a, b, c, f(c)])

        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return np.array(steps)

# Step 3: Run everything
a, b = find_initial_interval()
print(f"Initial interval: [{a:.4f}, {b:.4f}]")

steps_array = bisection_method(f, a, b)

# Step 4: Plotting
x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = x^3 - x - 2')
plt.axhline(0, color='black', linestyle='--')

# Plot all midpoints (roots)
for i, step in enumerate(steps_array):
    c = step[2]
    plt.plot(c, f(c), 'ro', markersize=4)
    plt.text(c, f(c), f'{i+1}', fontsize=8)

plt.title("Bisection Method Root-Finding Process")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

# Optional: Print steps
print("\nBisection steps (a, b, c, f(c)):")
print(steps_array)
