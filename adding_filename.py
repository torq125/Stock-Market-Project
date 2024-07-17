import pandas as pd
import os

# Directory containing the CSV files
directory = 'all_csv_files'

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Full path to the CSV file
        file_path = os.path.join(directory, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Add a new column with the filename (without extension)
        df['filename'] = os.path.splitext(filename)[0]

        # Save the modified DataFrame back to CSV
        df.to_csv(file_path, index=False)

        # Print the filename to track progress
        print(f"Added 'filename' column to: {filename}")

print("New column added to all CSV files.")
