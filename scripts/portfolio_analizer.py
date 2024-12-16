from pypfopt import expected_returns, risk_models, EfficientFrontier
import yfinance as yf

def calculate_portfolio_weights(tickers, start_date, end_date):
    """
    Calculate the optimal portfolio weights using the Maximum Sharpe Ratio.

    Parameters:
    - tickers (list of str): List of stock ticker symbols.
    - start_date (str): Start date for the historical data in 'YYYY-MM-DD' format.
    - end_date (str): End date for the historical data in 'YYYY-MM-DD' format.

    Returns:
    - dict: Optimal weights for each ticker.
    """
    # Fetch closing price data
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    
    # Calculate expected returns and covariance matrix
    mu = expected_returns.mean_historical_return(data)
    cov = risk_models.sample_cov(data)
    
    # Optimize portfolio
    ef = EfficientFrontier(mu, cov)
    weights = ef.max_sharpe()  # Maximize Sharpe Ratio
    weights = dict(zip(tickers, weights.values()))  # Convert weights to a dictionary
    
    return weights

def calculate_portfolio_performance(tickers, start_date, end_date):
    """
    Calculate the portfolio's expected return, volatility, and Sharpe ratio.

    Parameters:
    - tickers (list of str): List of stock ticker symbols.
    - start_date (str): Start date for the historical data in 'YYYY-MM-DD' format.
    - end_date (str): End date for the historical data in 'YYYY-MM-DD' format.

    Returns:
    - tuple: Portfolio return, volatility, and Sharpe ratio.
    """
    # Fetch closing price data
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    
    # Calculate expected returns and covariance matrix
    mu = expected_returns.mean_historical_return(data)
    cov = risk_models.sample_cov(data)
    
    # Optimize portfolio
    ef = EfficientFrontier(mu, cov)
    ef.max_sharpe()  # Maximize Sharpe Ratio
    
    # Get portfolio performance metrics
    portfolio_return, portfolio_volatility, sharpe_ratio = ef.portfolio_performance()
    
    return portfolio_return, portfolio_volatility, sharpe_ratio