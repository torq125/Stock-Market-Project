import pandas as pd
import os

# Path to your CSV file containing security codes and company names
csv_file_path = 'bse_securities.csv'
# Path to the folder containing the files to rename
folder_path = 'all_csv_files'
# Define the start and end of the range

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

start_row = 2309 #2311-2 because of 0 based indexing and header row
end_row = 2638

# Iterate through the specified range
for index in range(start_row, end_row + 1):  # end_row + 1 because the end is inclusive
    print(f'Accessing index: {index}')
    row = df.iloc[index]  # Get the specific row

    security_code = row[0]  # Assuming security code is in the first column
    company_name = row[1]    # Assuming company name is in the second column

    # Define the old file name and new file name
    old_file_name = f"{security_code}.csv"
    new_file_name = f"{company_name}.csv"

    # Create full paths for old and new file names
    old_file_path = os.path.join(folder_path, old_file_name)
    new_file_path = os.path.join(folder_path, new_file_name)

    # Check if the old file exists and rename it
    if os.path.exists(old_file_path):
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {old_file_name} to {new_file_name}')
    else:
        print(f'File not found: {old_file_name}')