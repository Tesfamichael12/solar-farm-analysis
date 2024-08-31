import streamlit as st
import pandas as pd
from data_loader import DataLoader
from eda import EDA
from sentiment_analysis import SentimentAnalysis
from technical_indicators import TechnicalIndicators
from correlation_analysis import CorrelationAnalysis

# Load data
data_loader = DataLoader(news_data_path='data/news_data.csv', stock_data_path='data/stock_data.csv')
news_df = data_loader.load_news_data()
stock_df = data_loader.load_stock_data()

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a page", ['EDA', 'Sentiment Analysis', 'Technical Indicators', 'Correlation Analysis'])

if options == 'EDA':
    st.title("Exploratory Data Analysis (EDA)")
    eda = EDA(news_df, stock_df)
    st.write("### Descriptive Statistics")
    st.write(eda.descriptive_statistics())
    
    st.write("### News Distribution Over Time")
    eda.plot_news_distribution()
    
    st.write("### Stock Price Over Time")
    eda.plot_stock_price()

elif options == 'Sentiment Analysis':
    st.title("Sentiment Analysis")
    sentiment_analyzer = SentimentAnalysis(news_df)
    sentiment_df = sentiment_analyzer.analyze_sentiment()
    st.write("### Sentiment Data")
    st.write(sentiment_df.head())

    st.write("### Sentiment Distribution")
    sentiment_analyzer.plot_sentiment_distribution()

elif options == 'Technical Indicators':
    st.title("Technical Indicators")
    ti = TechnicalIndicators(stock_df)
    stock_with_indicators = ti.calculate_indicators()
    st.write("### Stock Data with Indicators")
    st.write(stock_with_indicators.head())

    st.write("### Technical Indicators Plot")
    ti.plot_indicators()

elif options == 'Correlation Analysis':
    st.title("Correlation Analysis")
    correlation_analyzer = CorrelationAnalysis(news_df, stock_df)
    correlation = correlation_analyzer.calculate_correlation()
    st.write(f"### Correlation between Sentiment and Stock Price: {correlation}")
