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

if __name__ == "__main__":
    # Example usage
    import pandas as pd

    data_file = 'path/to/solar_radiation_data.csv'
    df = pd.read_csv(data_file)
    plot_time_series(df, 'GHI', 'Global Horizontal Irradiance Over Time')
    plot_correlation_matrix(df, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'])
    plot_histogram(df, 'WS')
