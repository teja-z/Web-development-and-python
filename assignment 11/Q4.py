import pandas as pd

# Example schedule: random presence of John and Judy over 10 days
df = pd.DataFrame({
    'John': [True, False, True, False, True, False, True, False, False, True],
    'Judy': [False, False, True, True, False, True, True, False, True, True]
})

# Step 1: Identify party days
df['party'] = df['John'] & df['Judy']

# Step 2: Create the days_til_party column, filled with a placeholder
days = len(df)
days_til_party = [None] * days

# Step 3: Loop backward to fill in countdown to next party
next_party = float('inf')
for i in reversed(range(days)):
    if df.loc[i, 'party']:
        next_party = 0
    days_til_party[i] = next_party
    if next_party != float('inf'):
        next_party += 1

# Step 4: Add to DataFrame
df['days_til_party'] = days_til_party

# Optional: Drop the helper 'party' column
df.drop(columns='party', inplace=True)

print(df)
