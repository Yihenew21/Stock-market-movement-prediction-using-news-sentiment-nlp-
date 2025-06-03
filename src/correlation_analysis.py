import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List


def merge_sentiment_price(sentiment_df, price_df, date_col='date', how='inner'):
    """
    Merge sentiment and price data on the specified date column.
    
    Parameters:
    - sentiment_df: DataFrame containing sentiment data with a date column.
    - price_df: DataFrame containing price data with a date column.
    - date_col: Name of the date column in both DataFrames (default: 'date').
    - how: Type of merge ('inner', 'outer', 'left', 'right') (default: 'inner').
    
    Returns:
    - Merged DataFrame containing both sentiment and price data.
    """
    try:
        # Ensure date columns are datetime and timezone-naive
        sentiment_df[date_col] = pd.to_datetime(sentiment_df[date_col], errors='coerce').dt.tz_localize(None)
        price_df[date_col] = pd.to_datetime(price_df[date_col], errors='coerce').dt.tz_localize(None)
        
        # Merge DataFrames
        merged_df = pd.merge(
            sentiment_df,
            price_df,
            on=date_col,
            how=how
        )
        return merged_df
    except Exception as e:
        raise Exception(f"Error merging sentiment and price data: {e}")


def compute_correlations(df: pd.DataFrame, cols1: List[str], cols2: List[str], method: str = 'pearson') -> pd.DataFrame:
    """
    Compute correlation matrix between two sets of columns.
    Args:
        df (pd.DataFrame): DataFrame containing columns.
        cols1 (List[str]): First set of columns.
        cols2 (List[str]): Second set of columns.
        method (str): 'pearson' or 'spearman'.
    Returns:
        pd.DataFrame: Correlation matrix (cols1 x cols2).
    """
    corr = pd.DataFrame(index=cols1, columns=cols2)
    for c1 in cols1:
        for c2 in cols2:
            corr.loc[c1, c2] = df[c1].corr(df[c2], method=method)
    return corr.astype(float)


def plot_correlation_heatmap(corr_df: pd.DataFrame, title: str = 'Correlation Heatmap'):
    """
    Plot a heatmap of the correlation matrix.
    Args:
        corr_df (pd.DataFrame): Correlation matrix.
        title (str): Plot title.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', center=0)
    plt.title(title)
    plt.tight_layout()
    plt.show()

# Example usage:
# merged = merge_sentiment_price(sentiment_df, price_df)
# corr = compute_correlations(merged, ['sentiment_compound'], ['daily_return', 'SMA_20'])
# plot_correlation_heatmap(corr) 