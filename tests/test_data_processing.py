
import sys
import os
# Dynamically add the absolute path to the project directory and scripts
project_root = r"C:\Users\hp\Desktop\10Academy\Financial-News-and-Stock-Market-Analysis"
scripts_path = os.path.join(project_root, "scripts")

sys.path.append(project_root)  # Add project root to sys.path
sys.path.append(scripts_path)  # Add scripts directory to sys.path

from scripts.data_load import load_data, clean_data

def test_load_data():
    df = load_data('../Data/raw_analyst_rating.csv/raw_analyst_rating.csv')
    assert not df.empty, "Dataframe should not be empty"

def test_clean_data():
    df = load_data('../Data/raw_analyst_rating.csv/raw_analyst_rating.csv')
    df_cleaned = clean_data(df)
    assert df_cleaned['headline'].notnull().all(), "Headlines should not have null values"
    assert df_cleaned['date'].notnull().all(), "Dates should not have null values"
