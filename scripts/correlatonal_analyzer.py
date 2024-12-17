import yfinance as yf
import pandas as pd
import numpy as np
from textblob import TextBlob
import random


def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.
    
    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date for fetching data (YYYY-MM-DD).
        end_date (str): End date for fetching data (YYYY-MM-DD).
    
    Returns:
        pd.DataFrame: Stock data with Date as the index.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data['Daily Returns'] = stock_data['Close'].pct_change()
    stock_data.reset_index(inplace=True)
    return stock_data[['Date', 'Close', 'Daily Returns']]




def generate_random_headlines(news_data, ticker=None, num_headlines=5):
    """
    Generate random headlines from news data.

    Args:
        news_data (pd.DataFrame): DataFrame containing news headlines and stock information.
        ticker (str, optional): Stock ticker to filter headlines. If None, headlines are chosen from all tickers.
        num_headlines (int): Number of random headlines to generate.

    Returns:
        list: List of randomly chosen headlines.
    """
    # Filter news data for a specific ticker, if provided
    if ticker:
        filtered_news = news_data[news_data['stock'] == ticker]
    else:
        filtered_news = news_data
    
    # Ensure there are enough headlines to sample
    if len(filtered_news) == 0:
        print("No headlines available for the specified ticker.")
        return []
    
    # Randomly select headlines
    headlines = filtered_news['headline'].dropna().tolist()
    random_headlines = random.sample(headlines, min(num_headlines, len(headlines)))
    
    return random_headlines



def analyze_ticker_correlation(ticker, stock_data, news_data):
    """
    Analyze the correlation between sentiment scores and stock data for a specific ticker.

    Args:
        ticker (str): Stock ticker symbol.
        stock_data (pd.DataFrame): Combined stock data with Ticker, Date, and Close.
        news_data (pd.DataFrame): News data with dates and headlines.

    Returns:
        dict: Correlation values:
            - 'sentiment_close': Correlation between sentiment and closing prices.
            - 'sentiment_returns': Correlation between sentiment and daily returns.
    """
    # Process data for the specific ticker
    ticker_data = process_ticker_data(ticker, stock_data, news_data)
    
    if ticker_data.empty:
        print(f"No data available for ticker: {ticker}")
        return {'sentiment_close': None, 'sentiment_returns': None}
    
    # Drop missing values to avoid issues during correlation
    ticker_data = ticker_data.dropna(subset=['Sentiment', 'Close', 'Daily Returns'])

    # Calculate correlations
    correlation_close = ticker_data['Sentiment'].corr(ticker_data['Close'])
    correlation_returns = ticker_data['Sentiment'].corr(ticker_data['Daily Returns'])
    
    # Return the correlation results
    return {
        'sentiment_close': correlation_close,
        'sentiment_returns': correlation_returns
    }


def calculate_sentiment(text):
    """
    Calculate sentiment polarity for a given text.
    
    Args:
        text (str): The headline or text to analyze.
    
    Returns:
        float: Sentiment polarity score (-1 to 1).
    """
    return TextBlob(text).sentiment.polarity


def process_ticker_data(ticker, stock_data, news_data):
    """
    Process data for a specific ticker, calculate sentiment, and combine with stock data.
    
    Args:
        ticker (str): Stock ticker symbol.
        stock_data (pd.DataFrame): Combined stock data.
        news_data (pd.DataFrame): News data with headlines and dates.
    
    Returns:
        pd.DataFrame: DataFrame with Date, Headline, Sentiment, Close, and Daily Returns.
    """
    # Filter stock data for the specific ticker
    ticker_stock_data = stock_data[stock_data['Ticker'] == ticker].copy()
    
    # Normalize dates in stock data and news data
    ticker_stock_data['Date'] = pd.to_datetime(ticker_stock_data['Date'])
    news_data['Date'] = pd.to_datetime(news_data['date']).dt.date  # Ensure date alignment to trading day
    ticker_stock_data['Date'] = ticker_stock_data['Date'].dt.date  # Keep only the date part
    
    # Filter news data for the ticker
    ticker_news_data = news_data[news_data['stock'] == ticker].copy()
    
    # Calculate sentiment for each headline
    ticker_news_data['Sentiment'] = ticker_news_data['headline'].apply(calculate_sentiment)
    
    # Merge news data with stock data on the date
    combined_ticker_data = pd.merge(
        ticker_stock_data[['Date', 'Close']],
        ticker_news_data[['Date', 'Sentiment']],
        on='Date',
        how='inner'
    )
    
    # Calculate daily returns
    combined_ticker_data['Daily Returns'] = combined_ticker_data['Close'].pct_change()
    
    return combined_ticker_data


def analyze_tickers(combined_data, news_data, output_path):
    """
    Analyze sentiment and stock movements for all tickers and save the results.
    
    Args:
        combined_data (pd.DataFrame): Stock price data with tickers.
        news_data (pd.DataFrame): News headlines data.
        output_path (str): Path to save the processed combined data.
    
    Returns:
        None
    """
    results = []
    tickers = combined_data['Ticker'].unique()
    
    for ticker in tickers:
        print(f"Processing data for ticker: {ticker}")
        
        # Process each ticker's data
        ticker_data = process_ticker_data(ticker, combined_data, news_data)
        results.append(ticker_data)
    
    # Combine all ticker data into one DataFrame
    final_combined_data = pd.concat(results, ignore_index=True)
    
    # Save the combined data
    final_combined_data.to_csv(output_path, index=False)
    print(f"Combined data saved to {output_path}")
