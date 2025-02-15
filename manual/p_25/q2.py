import pandas as pd
import numpy as np

# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Creating a Pandas Series from the NumPy array
series = pd.Series(arr)

# Displaying the Series
print("Pandas Series from NumPy Array:")
print(series)