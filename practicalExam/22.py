# Program using list in DataFrame data structure of panda.

import pandas as pd

# Creating a DataFrame from a list of lists
data = [[10, 'Alice', 85],
        [20, 'Bob', 90],
        [30, 'Charlie', 88],
        [40, 'David', 92],
        [50, 'Eve', 89]]

# Define column names
columns = ['Age', 'Name', 'Score']

# Creating the DataFrame
df = pd.DataFrame(data, columns=columns)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Accessing a specific column (e.g., 'Name')
print("\nNames of the students:")
print(df['Name'])

# Accessing a specific row by index (e.g., row with index 2)
print("\nDetails of the student at index 2:")
print(df.iloc[2])

# Accessing a specific cell (e.g., score of the student at index 1)
print("\nScore of the student at index 1:")
print(df.at[1, 'Score'])

# Adding a new column (e.g., 'Passed' based on the score)
df['Passed'] = df['Score'] >= 90

# Displaying the DataFrame after adding the new column
print("\nDataFrame after adding the 'Passed' column:")
print(df)

# Filtering the DataFrame (students who passed)
passed_students = df[df['Passed'] == True]
print("\nStudents who passed:")
print(passed_students)