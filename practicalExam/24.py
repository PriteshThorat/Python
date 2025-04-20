# Program using series in DataFrame data structure of panda.

import pandas as pd

# Creating Series
age = pd.Series([10, 20, 30, 40, 50], name='Age')
name = pd.Series(['Alice', 'Bob', 'Charlie', 'David', 'Eve'], name='Name')
score = pd.Series([85, 90, 88, 92, 89], name='Score')

# Creating a DataFrame by combining the Series
df = pd.concat([age, name, score], axis=1)

# Displaying the DataFrame
print("DataFrame created from Series:")
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