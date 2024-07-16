import pandas as pd
import os


def load_data(data_path, columns=None):
    data = pd.read_csv(data_path)
    if columns:
        data = data[columns]
    return data


data_paths = [f for f in os.listdir("all_csv_files") if f.endswith('.csv')]

specific_columns = ['Date', 'Open Price', 'High Price', 'Low Price', 'Close Price', 'No.of Shares', 'No. of Trades']

for data_path in data_paths:
    # Load the data for each file
    data = load_data(os.path.join("all_csv_files", data_path), columns=specific_columns)

    # Optionally: perform any operations or modifications on 'data' here

    # Save the updated DataFrame back to the same CSV file
    data.to_csv(os.path.join("all_csv_files", data_path), index=False)

# Optional: Print the number of files updated
print(f"Updated {len(data_paths)} CSV files.")
