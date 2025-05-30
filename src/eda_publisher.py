"""
eda_publisher.py
Module for publisher analysis on analyst ratings dataset.
"""
import pandas as pd
from collections import Counter
import re

def top_publishers(df, publisher_col="publisher", top_n=10):
    """
    Identify the top publishers by article count.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        publisher_col (str): Name of the column with publisher info.
        top_n (int): Number of top publishers to return.
    Returns:
        pd.Series: Top publishers and their article counts.
    """
    return df[publisher_col].value_counts().head(top_n)


def publisher_domains(df, publisher_col="publisher", top_n=10):
    """
    If publisher names are emails, extract unique domains and count their frequency.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        publisher_col (str): Name of the column with publisher info.
        top_n (int): Number of top domains to return.
    Returns:
        List[Tuple[str, int]]: List of (domain, count) tuples.
    """
    # Extract domains from email addresses
    emails = df[publisher_col].astype(str)
    domains = emails.apply(lambda x: re.findall(r"@([\w\.-]+)", x)).explode().dropna()
    return Counter(domains).most_common(top_n) 