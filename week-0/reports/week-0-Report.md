# Solar Farm Data Analysis Assignment

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Dependencies](#dependencies)
4. [Application Code](#application-code)
   - [app/\_\_init\_\_.py](#appinitpy)
   - [app/dashboard.py](#appdashboardpy)
5. [Scripts](#scripts)
   - [scripts/\_\_init\_\_.py](#scriptsinitpy)
   - [scripts/data_processing.py](#scriptsdata_processingpy)
   - [scripts/visualization.py](#scriptsvisualizationpy)
6. [Testing](#testing)
   - [tests/\_\_init\_\_.py](#testsinitpy)
   - [tests/test_data.py](#teststest_datapy)
7. [Conclusion](#conclusion)

## Introduction

This project aims to analyze solar farm data using Python. The tasks include data loading, cleaning, preprocessing, visualization, and unit testing. The project is organized into different modules for better structure and maintainability.

## Project Structure

The project is organized as follows:

```plaintext
solar-farm-analysis/
├── app/
│   ├── __init__.py
│   └── dashboard.py
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── __init__.py
│   ├── data_processing.py
│   └── visualization.py
├── tests/
│   ├── __init__.py
│   └── test_data.py
├── requirements.txt
└── README.md
```

- app/: Contains the main application code, including the dashboard setup.
- data/: Stores raw and processed data files.
  scripts/: Includes scripts for data processing and visualization.
- tests/: Contains unit tests for verifying the functionality of data processing scripts.
- requirements.txt: Lists the dependencies needed to run the project.
- README.md: Provides an overview of the project.

# Dependencies

All dependencies are listed in the requirements.txt file. To install them, run:

The main dependencies include:

- pandas: For data manipulation.
- matplotlib: For data visualization.
- seaborn: For enhanced data visualization.
- pytest: For running unit tests.
- streamlit: For building the dashboard.

# Application Code

## app/dashboard.py

```python

import streamlit as st
import pandas as pd
from scripts.data_processing import load_data, clean_data, preprocess_data
from scripts.visualization import plot_time_series, plot_correlation_matrix, plot_histogram

# Load and preprocess the data
df = load_data('data/processed/solar_data.csv')
df = clean_data(df)
df = preprocess_data(df)

# Streamlit app layout
st.title("Solar Farm Data Analysis Dashboard")

# Sidebar for user input
st.sidebar.header("Visualization Settings")
visualization_type = st.sidebar.selectbox("Select visualization type", ('Time Series', 'Correlation Matrix', 'Histogram'))

# Conditional rendering based on user input
if visualization_type == 'Time Series':
    column = st.sidebar.selectbox("Select column for Time Series", df.columns[1:])
    plot_time_series(df, column, f"{column} Over Time")

elif visualization_type == 'Correlation Matrix':
    columns = st.sidebar.multiselect("Select columns for Correlation Matrix", df.columns[1:])
    if columns:
        plot_correlation_matrix(df, columns)

elif visualization_type == 'Histogram':
    column = st.sidebar.selectbox("Select column for Histogram", df.columns[1:])
    plot_histogram(df, column)
```

# Scripts

## scripts/data_processing.py

```python
# scripts/data_processing.py

import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean the dataset by handling missing values and duplicates."""
    df = df.dropna()  # Remove rows with missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    print("Data cleaned successfully.")
    return df

def preprocess_data(df):
    """Preprocess the dataset by converting data types and extracting relevant features."""
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['GHI'] = df['GHI'].astype(float)
    print("Data preprocessed successfully.")
    return df

```

## scripts/visualization.py

```python

# scripts/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, column, title):
    """Plot a time series graph for a specific column."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df[column])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.grid(True)
    plt.show()

def plot_correlation_matrix(df, columns):
    """Plot a correlation matrix for selected columns."""
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_histogram(df, column, bins=20):
    """Plot a histogram for a specific column."""
    plt.figure(figsize=(8, 6))
    plt.hist(df[column], bins=bins, color='blue', alpha=0.7)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

```

# Testing

## tests/test_data.py

```python
# tests/test_data.py

import unittest
import pandas as pd
from scripts.data_processing import load_data, clean_data, preprocess_data

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures, if any."""
        self.file_path = 'data/processed/solar_data.csv'
        self.df = pd.DataFrame({
            'Timestamp': ['2024-08-01 00:00:00', '2024-08-01 01:00:00', '2024-08-01 02:00:00'],
            'GHI': [100, 200, 300],
            'DNI': [50, 100, 150]
        })

    def test_load_data(self):
        """Test loading data from CSV."""
        df_loaded = load_data(self.file_path)
        self.assertIsNotNone(df_loaded)

    def test_clean_data(self):
        """Test data cleaning by removing missing values and duplicates."""
        df_cleaned = clean_data(self.df)
        self.assertEqual(df_cleaned.shape[0], 3)

    def test_preprocess_data(self):
        """Test data preprocessing like converting data types."""
        df_cleaned = clean_data(self.df)
        df_preprocessed = preprocess_data(df_cleaned)
        self.assertEqual(df_preprocessed['Timestamp'].dtype, '<M8[ns]')
```

# Conclusion

This project provides a comprehensive framework for analyzing solar farm data using Python. The modular structure allows for easy maintenance and extension. The data processing scripts ensure that the data is loaded, cleaned, and preprocessed correctly, while the visualization scripts help in understanding the patterns and correlations in the data. The tests ensure the reliability and correctness of the data processing functions.
