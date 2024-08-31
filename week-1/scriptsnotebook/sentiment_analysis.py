from textblob import TextBlob
import pandas as pd

class SentimentAnalysis:
    def __init__(self, news_df: pd.DataFrame):
        self.news_df = news_df

    def analyze_sentiment(self) -> pd.DataFrame:
        """Performs sentiment analysis on news headlines."""
        self.news_df['Sentiment'] = self.news_df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
        return self.news_df

    def plot_sentiment_distribution(self):
        """Plots sentiment distribution."""
        self.news_df['Sentiment'].hist(bins=50)
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Frequency')
        plt.show()
