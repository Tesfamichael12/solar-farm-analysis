import pandas as pd

class CorrelationAnalysis:
    def __init__(self, news_df: pd.DataFrame, stock_df: pd.DataFrame):
        self.news_df = news_df
        self.stock_df = stock_df

    def calculate_correlation(self) -> float:
        """Calculates correlation between sentiment and stock movement."""
        merged_df = pd.merge(self.news_df, self.stock_df, left_on='date', right_on='Date')
        correlation = merged_df['Sentiment'].corr(merged_df['Close'])
        print(f"Correlation between sentiment and stock price: {correlation}")
        return correlation
