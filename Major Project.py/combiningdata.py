import pandas as pd
import os

def load_data(data_path, columns=None):
    try:
        data = pd.read_csv(data_path)
        if data.empty:
            print(f"Warning: {data_path} is empty.")
            return None
        if columns:
            missing_columns = [col for col in columns if col not in data.columns]
            if missing_columns:
                print(f"Warning: Missing columns {missing_columns} in file {data_path}")
            data = data[[col for col in columns if col in data.columns]]
        return data
    except pd.errors.EmptyDataError:
        print(f"Warning: {data_path} is empty and will be skipped.")
        return None

data_paths = [f for f in os.listdir("./Temp data") if f.endswith('.csv')]

specific_columns = ['Date', 'Open Price', 'High Price', 'Low Price', 'Close Price', 'No.of Shares', 'No. of Trades']

data_frames = []
for data_path in data_paths:
    data = load_data(os.path.join("./Temp data", data_path), columns=specific_columns)
    if data is not None:
        data_frames.append(data)

if data_frames:
    new_df = pd.concat(data_frames, ignore_index=True)
    new_df.to_csv("./Temp data/combined_data.csv", index=False)
    print(f"Combined data has {len(new_df)} rows.")
else:
    print("No data to concatenate.")

