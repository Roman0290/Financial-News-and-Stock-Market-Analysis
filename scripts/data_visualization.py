import matplotlib.pyplot as plt
import seaborn as sns

def plot_headline_length_distribution(df):
    """Visualize the distribution of headline lengths"""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['headline_length'], bins=30, kde=True)
    plt.title('Distribution of Headline Lengths')
    plt.xlabel('Headline Length')
    plt.ylabel('Frequency')
    plt.show()

def plot_sentiment_distribution(df):
    """Visualize the sentiment distribution (Positive, Negative, Neutral)"""
    plt.figure(figsize=(10, 6))
    sentiment_counts = df['sentiment_category'].value_counts()
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
    plt.title('Sentiment Distribution of Headlines')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

def plot_articles_per_publisher(df):
    """Visualize the number of articles per publisher"""
    plt.figure(figsize=(12, 6))
    publisher_counts = df['publisher'].value_counts().head(10)  # Top 10 publishers
    sns.barplot(x=publisher_counts.index, y=publisher_counts.values)
    plt.title('Top 10 Publishers by Number of Articles')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.show()

def plot_publication_frequency(df):
    """Visualize publication frequency over time"""
    plt.figure(figsize=(10, 6))
    df_resampled = df.resample('D').size()
    df_resampled.plot()
    plt.title('Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles Published')
    plt.show()

import matplotlib.pyplot as plt

def visualize_time_series_analysis(df):
    """Visualize the frequency of articles published per day"""
    # Resample the data by day and count the number of articles published each day
    df_resampled = df.resample('D').size()
    
    # Plot the time series data
    plt.figure(figsize=(12, 6))
    df_resampled.plot(title="Articles Published Per Day", color='blue')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles Published')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def plot_time_series(daily_counts):
    """Visualize publication frequency over time"""
    plt.figure(figsize=(10, 6))
    daily_counts.plot(kind='line', color='blue', linestyle='-', marker='o')
    plt.title("Daily Article Publication Frequency")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles Published")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

