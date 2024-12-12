import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from scripts.data_visualization import plot_headline_length_distribution, plot_sentiment_distribution, plot_articles_per_publisher, plot_publication_frequency


def headline_statistics(df):
    """Generate headline length statistics"""
    df['headline_length'] = df['headline'].apply(len)
    print("Headline Length Statistics:")
    print(df['headline_length'].describe())  # Simply print the statistics

def publisher_activity(df):
    """Count articles per publisher"""
    articles_per_publisher = df.groupby('publisher').size()
    print("Articles Per Publisher:")
    print(articles_per_publisher)

def publication_frequency(df):
    """Analyze the frequency of publications over time"""
    df.set_index('date', inplace=True)
    articles_per_day = df.resample('D').size()
    print("Articles Published Per Day:")
    print(articles_per_day)

def sentiment_analysis(df):
    """Perform sentiment analysis on headlines"""
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['sentiment_category'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
    print("Sentiment Categories:")
    print(df[['headline', 'sentiment_category']].head())

def topic_modeling(df):
    """Perform topic modeling using TF-IDF"""
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['headline'])
    tfidf_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    print("TF-IDF Topic Modeling Output:")
    print(tfidf_df.head())

def publisher_analysis(df):
    """Analyze publishers' contributions and domains"""
    df['publisher_domain'] = df['publisher'].str.extract(r'@([a-zA-Z0-9.-]+)')
    publisher_domains = df['publisher_domain'].value_counts()
    print("Publisher Domain Frequency:")
    print(publisher_domains)
def visualize_time_series_analysis(df):
    """Visualize the publication frequency of articles over time"""
    plt.figure(figsize=(10, 6))
    df_resampled = df.resample('D').size()  # Resample by day
    df_resampled.plot()
    plt.title('Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles Published')
    plt.show()


def visualize_sentiment_over_time(df):
    """Visualize sentiment trends over time."""
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['sentiment_category'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
    
    # Resample to daily sentiment average
    sentiment_per_day = df.resample('D')['sentiment'].mean()
    
    plt.figure(figsize=(10, 6))
    sentiment_per_day.plot(label='Daily Sentiment', color='green')
    
    plt.title('Sentiment Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Sentiment')
    plt.show()
# analysis.py



def check_stationarity(data):
    """Check if time series data is stationary using ADF test"""
    result = adfuller(data)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    return result[1]  # Return p-value for further analysis

def arima_model(data):
    """Fit ARIMA model and make forecast"""
    model = sm.tsa.ARIMA(data, order=(1,1,1))  # Change p, d, q based on your analysis
    model_fit = model.fit()
    
    forecast = model_fit.forecast(steps=12)  # Forecast next 12 steps
    return forecast

