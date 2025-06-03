import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def score_headlines_vader(df: pd.DataFrame, text_col: str = 'headline') -> pd.DataFrame:
    """
    Adds sentiment scores to a DataFrame of news headlines using VADER.
    Args:
        df (pd.DataFrame): DataFrame containing news headlines.
        text_col (str): Name of the column containing text to analyze.
    Returns:
        pd.DataFrame: Original DataFrame with new columns: 'sentiment_neg', 'sentiment_neu', 'sentiment_pos', 'sentiment_compound'.
    """
    analyzer = SentimentIntensityAnalyzer()
    # Handle missing values
    df = df.copy()
    df[text_col] = df[text_col].fillna("")
    sentiments = df[text_col].apply(analyzer.polarity_scores)
    df['sentiment_neg'] = sentiments.apply(lambda x: x['neg'])
    df['sentiment_neu'] = sentiments.apply(lambda x: x['neu'])
    df['sentiment_pos'] = sentiments.apply(lambda x: x['pos'])
    df['sentiment_compound'] = sentiments.apply(lambda x: x['compound'])
    return df

# Example usage:
# df = pd.read_csv('news.csv')
# df = score_headlines_vader(df, text_col='headline') 