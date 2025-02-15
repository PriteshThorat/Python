import pandas as pd

# Creating a Pandas Series with custom index labels
data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Accessing elements using index position (Use .iloc[])
print("Element at index 2:", data.iloc[2])

# Accessing elements using index label (No change needed)
print("Element at index 'c':", data['c'])

# Accessing multiple elements using index positions (Use .iloc[])
print("Elements at index 1 and 3:\n", data.iloc[[1, 3]])

# Accessing multiple elements using index labels (No change needed)
print("Elements at index 'b' and 'e':\n", data[['b', 'e']])