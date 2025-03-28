import pandas as pd

class MeanReversionStrategy:
    def __init__(self, prices, window=20):
        self.prices = prices
        self.window = window
        if isinstance(prices, pd.Series):
            self.prices_df = prices.to_frame()
        else:
            self.prices_df = prices
        self.mean = self.prices_df.rolling(window=window).mean()
        self.std = self.prices_df.rolling(window=window).std()
        self.upper_band = self.mean + 2 * self.std
        self.lower_band = self.mean - 2 * self.std

    def generate_signals(self):
        signals = []
        for i in range(len(self.prices)):
            if pd.notna(self.upper_band.iloc[i]) and self.prices.iloc[i] > self.upper_band.iloc[i]:  
                signals.append('SELL')
            elif pd.notna(self.lower_band.iloc[i]) and self.prices.iloc[i] < self.lower_band.iloc[i]:  
                signals.append('BUY')
            else:
                signals.append('HOLD')
        return signals