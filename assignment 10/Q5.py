import numpy as np

# Example NumPy array of strings
arr = np.array(["apple", "banana", "kiwi", "watermelon", "grape"])

# Function to justify strings
def format_array(arr, mode="center"):
    formatted = []
    for item in arr:
        if mode == "center":
            formatted.append(item.center(15, "_"))
        elif mode == "left":
            formatted.append(item.ljust(15, "_"))
        elif mode == "right":
            formatted.append(item.rjust(15, "_"))
        else:
            raise ValueError("Mode must be 'center', 'left', or 'right'")
    return np.array(formatted)

# Format the array in different modes
centered = format_array(arr, "center")
left = format_array(arr, "left")
right = format_array(arr, "right")

# Output
print("Centered:\n", centered)
print("\nLeft-Justified:\n", left)
print("\nRight-Justified:\n", right)
