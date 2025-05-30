"""
eda_text.py
Module for text analysis and topic modeling on analyst ratings dataset.
"""
import pandas as pd
from collections import Counter
import nltk
from sklearn.feature_extraction.text import CountVectorizer


def extract_keywords(df, text_col="headline", top_n=20):
    """
    Extract the most common keywords from the text column.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        text_col (str): Name of the column with text data.
        top_n (int): Number of top keywords to return.
    Returns:
        List[Tuple[str, int]]: List of (keyword, count) tuples.
    """
    # Tokenize and clean text
    nltk.download('stopwords', quiet=True)
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    words = (
        df[text_col]
        .astype(str)
        .str.lower()
        .str.replace(r"[^a-zA-Z0-9 ]", "", regex=True)
        .str.split()
    )
    # Flatten list and remove stopwords
    all_words = [word for sublist in words for word in sublist if word not in stop_words]
    # Count most common
    return Counter(all_words).most_common(top_n)


def simple_topic_modeling(df, text_col="headline", n_topics=5, n_words=10):
    """
    Perform simple topic modeling using CountVectorizer and extract top words per topic.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        text_col (str): Name of the column with text data.
        n_topics (int): Number of topics to extract.
        n_words (int): Number of top words per topic.
    Returns:
        List[List[str]]: List of topics, each as a list of top words.
    """
    # Vectorize the text
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english', max_features=1000)
    X = vectorizer.fit_transform(df[text_col].astype(str))
    # Use Latent Dirichlet Allocation for topic modeling
    from sklearn.decomposition import LatentDirichletAllocation
    lda = LatentDirichletAllocation(
    n_components=n_topics,
    random_state=42,
    learning_method='online',  # Faster for large datasets
    max_iter=5,                # Fewer iterations for speed
    batch_size=128             # Smaller batches for speed
    )
    lda.fit(X)
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(lda.components_):
        top_features = [feature_names[i] for i in topic.argsort()[:-n_words - 1:-1]]
        topics.append(top_features)
    return topics
