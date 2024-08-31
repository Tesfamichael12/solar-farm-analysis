# scripts/data_loader.py

import pandas as pd
import os
from typing import Dict

class DataLoader:
    def __init__(self, news_data_path: str = "../data/raw_analysis.csv", stock_data_folder: str = "../data"):
        """
        Initializes the DataLoader with paths to the news data and stock data folder.

        Args:
        - news_data_path (str): Path to the financial news CSV file.
        - stock_data_folder (str): Path to the folder containing stock price CSV files.
        """
        self.news_data_path = news_data_path
        self.stock_data_folder = stock_data_folder

    def load_news_data(self) -> pd.DataFrame:
        """
        Loads financial news data from a CSV file.

        Returns:
        - pd.DataFrame: DataFrame containing the news data.
        """
        news_df = pd.read_csv(self.news_data_path)
        news_df['date'] = pd.to_datetime(news_df['date'])
        return news_df

    def load_stock_data(self, stock_symbol: str) -> pd.DataFrame:
        """
        Loads stock price data for a specific stock from a CSV file.

        Args:
        - stock_symbol (str): The stock symbol (e.g., 'AAPL').

        Returns:
        - pd.DataFrame: DataFrame containing the stock price data.
        """
        stock_file_path = os.path.join(self.stock_data_folder, f"{stock_symbol}.csv")
        
        if not os.path.exists(stock_file_path):
            raise FileNotFoundError(f"Stock data file for {stock_symbol} not found at {stock_file_path}")

        stock_df = pd.read_csv(stock_file_path)
        stock_df['Date'] = pd.to_datetime(stock_df['Date'])
        return stock_df

    def load_all_stock_data(self) -> Dict[str, pd.DataFrame]:
        """
        Loads all stock price data files in the specified folder.

        Returns:
        - dict: A dictionary where the keys are stock symbols and the values are DataFrames of stock data.
        """
        stock_data = {}
        for file_name in os.listdir(self.stock_data_folder):
            if file_name.endswith('.csv'):
                stock_symbol = file_name.split('.')[0]
                stock_df = self.load_stock_data(stock_symbol)
                stock_data[stock_symbol] = stock_df
                print(f"Loaded data for {stock_symbol}")

        return stock_data
