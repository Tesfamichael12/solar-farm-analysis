import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EDA:
    def __init__(self, news_df: pd.DataFrame, stock_df: pd.DataFrame):
        self.news_df = news_df
        self.stock_df = stock_df

    def descriptive_statistics(self):
        """Displays basic statistics for the dataset."""
        print("News Data Statistics:")
        print(self.news_df.describe(include='all'))
        print("\nStock Data Statistics:")
        print(self.stock_df.describe())

    def plot_news_distribution(self):
        """Plots distribution of news over time."""
        self.news_df['date'].dt.to_period('M').value_counts().sort_index().plot(kind='bar')
        plt.title('News Distribution Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.show()

    def plot_stock_price(self):
        """Plots stock price over time."""
        plt.figure(figsize=(14, 7))
        sns.lineplot(data=self.stock_df, x='Date', y='Close', label='Close Price')
        plt.title('Stock Price Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()
