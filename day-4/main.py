import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from collections import deque
import sys
import os
# %run order_book.py
# Add the current directory to path to ensure imports work
sys.path.append(os.path.abspath('.'))

# Import our custom modules
from order_book import OrderBook
from mean_reversion import MeanReversionStrategy

# Create an instance of the order book
book = OrderBook()

# Add some sample orders
print("Adding orders to the book...")
book.add_order(price=100.0, quantity=10, side='buy')
book.add_order(price=101.0, quantity=5, side='buy')
book.add_order(price=99.0, quantity=7, side='buy')
book.add_order(price=102.0, quantity=3, side='sell')
book.add_order(price=103.0, quantity=8, side='sell')
book.add_order(price=101.5, quantity=4, side='sell')

# Print the current order book state
book.output()

# Match orders
print("\nMatching orders...")
book.match_orders()

# Print the order book after matching
print("\nOrder book after matching:")
book.output()

# Load historical stock data
print("Loading historical stock data...")
stock_data = yf.download('AAPL', start='2020-01-01', end='2022-01-01')
print(f"Loaded {len(stock_data)} days of data")
stock_data.head()


# Create and apply the mean reversion strategy
strategy = MeanReversionStrategy(stock_data['Close'])
signals = strategy.generate_signals()
stock_data['Signal'] = signals

# Display the first few rows of the data with signals
print("\nStock data with signals:")
display(stock_data.head())

# Plot the strategy
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Stock Price', alpha=0.7)
plt.plot(strategy.mean, linestyle='-', color='blue', label='Mean', alpha=0.5)
plt.plot(strategy.upper_band, linestyle='dashed', color='red', label='Upper Bound')
plt.plot(strategy.lower_band, linestyle='dashed', color='green', label='Lower Bound')

# Mark buy and sell signals
buy_signals = stock_data[stock_data['Signal'] == 'BUY']
sell_signals = stock_data[stock_data['Signal'] == 'SELL']

plt.scatter(buy_signals.index, buy_signals['Close'], color='green', marker='^', s=100, label='Buy')
plt.scatter(sell_signals.index, sell_signals['Close'], color='red', marker='v', s=100, label='Sell')

plt.title('Mean Reversion Strategy for AAPL')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()