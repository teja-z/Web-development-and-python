import pandas as pd

# Create the Series (with correct quotes)
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert to upper case
upper_case = s.str.upper()
print("Upper case:\n", upper_case, "\n")

# Convert to lower case
lower_case = s.str.lower()
print("Lower case:\n", lower_case, "\n")

# Find the length of each string
lengths = s.str.len()
print("Length of strings:\n", lengths)
