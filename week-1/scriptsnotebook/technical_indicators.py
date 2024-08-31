import talib
import pandas as pd

class TechnicalIndicators:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

    def calculate_indicators(self) -> pd.DataFrame:
        """Calculates various technical indicators."""
        self.stock_df['SMA'] = talib.SMA(self.stock_df['Close'], timeperiod=30)
        self.stock_df['EMA'] = talib.EMA(self.stock_df['Close'], timeperiod=30)
        self.stock_df['RSI'] = talib.RSI(self.stock_df['Close'], timeperiod=14)
        self.stock_df['MACD'], self.stock_df['MACD_signal'], self.stock_df['MACD_hist'] = talib.MACD(
            self.stock_df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        return self.stock_df

    def plot_indicators(self):
        """Plots technical indicators."""
        plt.figure(figsize=(14, 7))
        sns.lineplot(data=self.stock_df, x='Date', y='SMA', label='SMA')
        sns.lineplot(data=self.stock_df, x='Date', y='EMA', label='EMA')
        plt.title('Stock Price with SMA and EMA')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()
