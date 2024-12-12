import pandas as pd

def load_data(file_path):
    """Load raw data from CSV file"""
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """Clean the dataset (handle missing values, date conversion, etc.)"""
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['headline', 'url', 'publisher', 'date'], inplace=True)
    return df
