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

if __name__ == "__main__":
    # Example usage
    data_file = 'path/to/solar_radiation_data.csv'
    df = load_data(data_file)
    if df is not None:
        df = clean_data(df)
        df = preprocess_data(df)
