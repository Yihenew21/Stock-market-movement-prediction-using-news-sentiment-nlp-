"""
eda_descriptive.py
Module for descriptive statistics on analyst ratings dataset.
"""
import pandas as pd
import matplotlib.pyplot as plt


def headline_length_stats(df, headline_col="headline"):
    """
    Compute basic statistics for the length of headlines.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        headline_col (str): Name of the column with headlines/text.
    Returns:
        pd.Series: Descriptive statistics (count, mean, std, min, 25%, 50%, 75%, max) for headline lengths.
    """
    # Calculate the length of each headline
    lengths = df[headline_col].astype(str).apply(len)
    # Return descriptive statistics
    return lengths.describe()


def articles_per_publisher(df, publisher_col="publisher"):
    """
    Count the number of articles per publisher.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        publisher_col (str): Name of the column with publisher info.
    Returns:
        pd.Series: Number of articles per publisher, sorted descending.
    """
    return df[publisher_col].value_counts()


def plot_articles_over_time(df, date_col="date", freq="D"):
    """
    Plot the number of articles published over time.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        date_col (str): Name of the column with publication dates.
        freq (str): Frequency for grouping (e.g., 'D' for day, 'M' for month).
    Returns:
        matplotlib.axes.Axes: The plot axes object.
    """
    # Convert date column to datetime
    dates = pd.to_datetime(df[date_col], errors="coerce")
    # Group by the specified frequency
    counts = dates.groupby(dates.dt.to_period(freq)).count()
    # Plot
    ax = counts.plot(kind="bar", figsize=(12, 4), title="Articles Published Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Number of Articles")
    plt.tight_layout()
    return ax
