"""
quant_indicators.py
Module for calculating technical indicators (SMA, EMA, RSI, MACD) using TA-Lib.
"""
import pandas as pd
import talib


def add_sma(df: pd.DataFrame, window: int = 20, price_col: str = 'Close') -> pd.DataFrame:
    """
    Add Simple Moving Average (SMA) to the DataFrame.
    Args:
        df (pd.DataFrame): DataFrame with stock data.
        window (int): Window size for SMA.
        price_col (str): Column to calculate SMA on.
    Returns:
        pd.DataFrame: DataFrame with new 'SMA_{window}' column.
    """
    df = df.copy()
    df[f'SMA_{window}'] = talib.SMA(df[price_col], timeperiod=window)
    return df


def add_ema(df: pd.DataFrame, window: int = 20, price_col: str = 'Close') -> pd.DataFrame:
    """
    Add Exponential Moving Average (EMA) to the DataFrame.
    Args:
        df (pd.DataFrame): DataFrame with stock data.
        window (int): Window size for EMA.
        price_col (str): Column to calculate EMA on.
    Returns:
        pd.DataFrame: DataFrame with new 'EMA_{window}' column.
    """
    df = df.copy()
    df[f'EMA_{window}'] = talib.EMA(df[price_col], timeperiod=window)
    return df


def add_rsi(df: pd.DataFrame, window: int = 14, price_col: str = 'Close') -> pd.DataFrame:
    """
    Add Relative Strength Index (RSI) to the DataFrame.
    Args:
        df (pd.DataFrame): DataFrame with stock data.
        window (int): Window size for RSI.
        price_col (str): Column to calculate RSI on.
    Returns:
        pd.DataFrame: DataFrame with new 'RSI_{window}' column.
    """
    df = df.copy()
    df[f'RSI_{window}'] = talib.RSI(df[price_col], timeperiod=window)
    return df


def add_macd(df: pd.DataFrame, price_col: str = 'Close') -> pd.DataFrame:
    """
    Add MACD (Moving Average Convergence Divergence) to the DataFrame.
    Args:
        df (pd.DataFrame): DataFrame with stock data.
        price_col (str): Column to calculate MACD on.
    Returns:
        pd.DataFrame: DataFrame with new 'MACD', 'MACD_signal', and 'MACD_hist' columns.
    """
    df = df.copy()
    macd, macd_signal, macd_hist = talib.MACD(df[price_col])
    df['MACD'] = macd
    df['MACD_signal'] = macd_signal
    df['MACD_hist'] = macd_hist
    return df
