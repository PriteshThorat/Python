import pandas as pd

# Creating a sample DataFrame
data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

# Writing DataFrame to a CSV file
df.to_csv('students.csv', index=False)  # 'index=False' to exclude index column

print("CSV file 'students.csv' has been created successfully!")

# Reading the CSV file into a DataFrame
df_read = pd.read_csv('students.csv')

# Displaying the DataFrame
print("\nData read from 'students.csv':")
print(df_read)