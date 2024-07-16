import pandas as pd
import requests
import csv


base_url = "https://www.nseindia.com/api/historical/cm/equity"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.nseindia.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive'
}

all_stock_data = []

with open('nse list.csv') as file:
    reader = csv.reader(file)
    header = 0
    for row in reader:
        if header == 0:
            header = 1
            continue
        if header == 331:
            break 
        header += 1 
        symbol = row[0]
        print(symbol)

        stock_data = pd.DataFrame()

        for start_year in range(2015, 2025):
            start_date = f"01-01-{start_year}"
            end_date = f"01-01-{start_year + 1}"
            url = f"{base_url}?symbol={symbol}&series=[%22EQ%22]&from={start_date}&to={end_date}"

           
            session = requests.Session()
            session.get("https://www.nseindia.com", headers=headers)

            
            response = session.get(url, headers=headers)
            print(response)

            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    df = pd.DataFrame(data['data'])
                    required_columns = ['CH_TIMESTAMP', 'CH_OPENING_PRICE', 'CH_TRADE_HIGH_PRICE',
                                        'CH_TRADE_LOW_PRICE', 'CH_CLOSING_PRICE', 'CH_TOT_TRADED_QTY', 'CH_TOTAL_TRADES']
                    if all(col in df.columns for col in required_columns):
                        df = df[required_columns]
                        df['Symbol'] = symbol  
                        all_stock_data.append(df)  
                    else:
                        print(f"Missing columns in data for symbol {symbol} for the period {start_date} to {end_date}")
                else:
                    print(f"No data found for symbol {symbol} for the period {start_date} to {end_date}")
            else:
                print(f"Failed to fetch data for symbol {symbol} for the period {start_date} to {end_date}")


final_stock_data = pd.concat(all_stock_data, ignore_index=True)


output_filename = 'nse_all_stock_data.csv'
final_stock_data.to_csv(output_filename, index=False)

print(f"All data saved to {output_filename}")
print(final_stock_data.head())