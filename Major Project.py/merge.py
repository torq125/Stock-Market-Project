import pandas as pd

# Load the first CSV file containing company names and security codes
company_file_path = 'Major Project.py\company_name.csv'
company_df = pd.read_csv(company_file_path)

# Load the second CSV file containing trading information
trading_file_path = 'Major Project.py\Complete_data.csv'
trading_df = pd.read_csv(trading_file_path)

# Merge the two dataframes on the 'Security Code' column
combined_df = pd.merge(trading_df, company_df, on='Security Code')

# Save the combined dataframe to a new CSV file
output_csv_path = 'combined_data.csv'
combined_df.to_csv(output_csv_path, index=False)

print(f"Combined data has been saved to {output_csv_path}.")
