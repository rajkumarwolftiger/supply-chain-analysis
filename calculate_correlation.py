import pandas as pd

# Read the dataset
df = pd.read_excel('q-excel-correlation-heatmap.xlsx')

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Save the matrix to a new CSV file
correlation_matrix.to_csv('correlation.csv')

print("Successfully created correlation.csv from the Excel file.")
