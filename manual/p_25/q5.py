import pandas as pd

# Creating a DataFrame from a List of Lists
data = [[1, 'Alice', 85], [2, 'Bob', 90], [3, 'Charlie', 78]]

# Defining column names
df = pd.DataFrame(data, columns=['ID', 'Name', 'Marks'])

# Displaying the DataFrame
print("DataFrame created using List of Lists:")
print(df)