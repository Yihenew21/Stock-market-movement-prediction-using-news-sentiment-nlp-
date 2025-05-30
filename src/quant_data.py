"""
quant_data.py
Module for loading and preparing yfinance stock data from multiple CSV files.
"""
import pandas as pd
import glob
import os
from typing import List

def load_yfinance_data(directory: str) -> pd.DataFrame:
    """
    Load all yfinance CSV files from a directory, add a 'Ticker' column, parse dates, and return a combined DataFrame.
    Args:
        directory (str): Path to the directory containing yfinance CSV files.
    Returns:
        pd.DataFrame: Combined DataFrame with all stock data and a 'Ticker' column.
    """
    # Find all CSV files in the directory
    csv_files = glob.glob(os.path.join(directory, '*.csv'))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in directory: {directory}")
    
    dfs = []  # <-- Fix: define dfs before the loop
    for file in csv_files:
        # Extract ticker from filename (e.g., 'AAPL_historical_data.csv' -> 'AAPL')
        ticker = os.path.splitext(os.path.basename(file))[0].replace('_historical_data', '')
        df = pd.read_csv(file)
        df['Ticker'] = ticker
        dfs.append(df)
    # Concatenate all DataFrames
    combined_df = pd.concat(dfs, ignore_index=True)
    # Parse 'Date' column to datetime
    if 'Date' in combined_df.columns:
        combined_df['Date'] = pd.to_datetime(combined_df['Date'])
    else:
        raise KeyError("'Date' column not found in the CSV files.")
    # Optional: Check for required columns
    required_cols = {'Open', 'High', 'Low', 'Close', 'Volume', 'Ticker', 'Date'}
    missing_cols = required_cols - set(combined_df.columns)
    if missing_cols:
        raise KeyError(f"Missing required columns: {missing_cols}")
    # Return the cleaned DataFrame
    return combined_df 