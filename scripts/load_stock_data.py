import os
import pandas as pd

def load_stock_data(data_folder):
    """
    Load stock data from CSV files in the specified folder, combine into a single DataFrame, 
    and return the combined DataFrame.

    Args:
        data_folder (str): Path to the folder containing stock data CSV files.

    Returns:
        pd.DataFrame: Combined DataFrame with all stock data.
    """
    # List all CSV files in the folder
    csv_files = [f for f in os.listdir(data_folder) if f.endswith('_historical_data.csv')]
    print("Files to load:", csv_files)

    all_data = []

    for file in csv_files:
        # Extract the stock ticker from the filename (e.g., 'AAPL' from 'AAPL_historical_data.csv')
        ticker = file.split('_')[0]

        # Load the data and add a 'Ticker' column
        file_path = os.path.join(data_folder, file)
        df = pd.read_csv(file_path, parse_dates=['Date'])
        df['Ticker'] = ticker  # Add a column for the stock ticker
        all_data.append(df)

    # Combine all data into a single DataFrame
    combined_data = pd.concat(all_data, ignore_index=True)

    # Drop rows with missing values
    combined_data.dropna(inplace=True)

    # Ensure 'Date' is of datetime type
    combined_data['Date'] = pd.to_datetime(combined_data['Date'], errors='coerce')

    return combined_data
