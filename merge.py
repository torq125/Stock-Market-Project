import pandas as pd
import os

# Directory containing the CSV files
directory = 'all_csv_files'
merged_file_path = 'merged_output.csv'  # Output file name

# List to hold DataFrames
dataframes = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Full path to the CSV file
        file_path = os.path.join(directory, filename)

        # Read the CSV file and append it to the list
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(merged_file_path, index=False)

print(f"Merged all CSV files into: {merged_file_path}")
