import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(filepath: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def inspect_data(data: pd.DataFrame) -> None:
    """Inspect the data."""
    print(data.head())
    print("Missing values:\n", data.isna().sum())
    print("Column names:\n", data.columns)

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values by dropping rows with missing values."""
    return data.dropna()

def normalize_columns(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Normalize specified columns using Min-Max scaling."""
    scaler = MinMaxScaler()
    data[columns] = scaler.fit_transform(data[columns])
    return data

def remove_outliers(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Remove outliers using the IQR method."""
    Q1 = data[columns].quantile(0.25)
    Q3 = data[columns].quantile(0.75)
    IQR = Q3 - Q1

    # Define outlier thresholds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = ((data[columns] < lower_bound) | (data[columns] > upper_bound)).any(axis=1)

    # Remove outliers
    return data[~outliers]

def convert_to_datetime(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """Ensure the data has a specified column in datetime format."""
    data[column] = pd.to_datetime(data[column])
    return data
