import pandas as pd
from pandas import DataFrame

class MeanReversionStrategy:
    def __init__(self, prices : DataFrame, window=20):
        self.prices = prices
        self.window = window
        # if isinstance(prices, pd.Series):
            # self.prices_df = prices.to_frame()
        # else:
            # self.prices_df = prices
        self.mean = self.prices.rolling(window=window).mean()
        self.std = self.prices.rolling(window=window).std()
        self.upper_band = self.mean + 2 * self.std
        self.lower_band = self.mean - 2 * self.std

    def generate_signals(self):
        signals = []
        col = self.prices.columns[0]  # Get the column name from DataFrame
        
        for i in range(len(self.prices)):
            # Get scalar values for comparison
            price = self.prices[col].iloc[i]
            upper_val = self.upper_band[col].iloc[i]
            lower_val = self.lower_band[col].iloc[i]
            
            # Handle NaN values in bands
            if pd.isna(upper_val) or pd.isna(lower_val):
                signals.append('HOLD')
                continue
                
            # Generate signals using scalar comparisons
            if price > upper_val:
                signals.append('SELL')
            elif price < lower_val:
                signals.append('BUY')
            else:
                signals.append('HOLD')
        return signals