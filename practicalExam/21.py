# Program using series data structure of Panda.

import pandas as pd

# Creating a Pandas Series from a list
data = [10, 20, 30, 40, 50]
labels = ['a', 'b', 'c', 'd', 'e']

series = pd.Series(data, index=labels)

# Displaying the Series
print("Original Series:")
print(series)

# Accessing a single element using its label
print("\nAccessing element with label 'c':", end=" ")
print(series['c'])

# Accessing elements using position (integer-based index)
print("\nAccessing element with position 2:", end=" ")
print(series.iloc[2])

# Adding a new element to the Series
series['f'] = 60
print("\nSeries after adding a new element:")
print(series)

# Performing basic arithmetic operation on the Series
series = series + 10  # Adding 10 to each element
print("\nSeries after adding 10 to each element:")
print(series)

# Filtering the Series (getting elements greater than 30)
filtered_series = series[series > 30]
print("\nFiltered Series (values > 30):")
print(filtered_series)