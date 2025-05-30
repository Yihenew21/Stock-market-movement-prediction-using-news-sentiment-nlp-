"""
eda_time.py
Module for time series analysis on analyst ratings dataset.
"""
import pandas as pd
import matplotlib.pyplot as plt

def publication_frequency(df, date_col="date", freq="D"):
    """
    Analyze and plot publication frequency over time.
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
    ax = counts.plot(kind="bar", figsize=(12, 4), title="Publication Frequency Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Number of Articles")
    plt.tight_layout()
    return ax

def publishing_time_distribution(df, date_col="date"):
    """
    Analyze and plot the distribution of publishing times (hour of day, day of week).
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        date_col (str): Name of the column with publication dates.
    Returns:
        Tuple[matplotlib.axes.Axes, matplotlib.axes.Axes]: Axes for hour and weekday plots.
    """
    # Convert date column to datetime
    dates = pd.to_datetime(df[date_col], errors="coerce")
    # Extract hour and weekday
    hours = dates.dt.hour
    weekdays = dates.dt.day_name()
    # Plot hour of day
    ax1 = hours.value_counts().sort_index().plot(kind="bar", figsize=(10, 3), title="Publishing Hour Distribution")
    ax1.set_xlabel("Hour of Day")
    ax1.set_ylabel("Number of Articles")
    plt.tight_layout()
    plt.show()
    # Plot day of week
    ax2 = weekdays.value_counts()[["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]].plot(kind="bar", figsize=(10, 3), title="Publishing Day Distribution")
    ax2.set_xlabel("Day of Week")
    ax2.set_ylabel("Number of Articles")
    plt.tight_layout()
    plt.show()
    return ax1, ax2 