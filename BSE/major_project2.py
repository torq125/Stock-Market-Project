import pandas as pd
import os

def load_data(data_path, columns=None):
    data = pd.read_csv(data_path)
    if columns:
        data = data[columns]
    return data

data_paths = [f for f in os.listdir("../temp_data") if f.endswith('.csv')]

specific_columns = ['Date', 'Open Price', 'High Price', 'Low Price', 'Close Price', 'No.of Shares', 'No. of Trades']  

data_frames = []
for data_path in data_paths:
    data = load_data(os.path.join("../temp_data", data_path), columns=specific_columns)
    data_frames.append(data)

new_df = pd.concat(data_frames, ignore_index=True)
new_df.to_csv("../temp_data/combined_data.csv", index=False)

print(len(new_df))