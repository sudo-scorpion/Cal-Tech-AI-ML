import pandas as pd
from typing import Tuple, List

def descriptive_statistics(data: pd.DataFrame, column: str) -> pd.Series:
    """Return descriptive statistics for a specified column."""
    return data[column].describe()

def group_sales_statistics(data: pd.DataFrame, group_column: str, sales_column: str) -> Tuple[str, str]:
    """Return the groups with highest and lowest sales."""
    group_sales = data.groupby(group_column)[sales_column].sum()
    highest_sales_group = group_sales.idxmax()
    lowest_sales_group = group_sales.idxmin()
    return highest_sales_group, lowest_sales_group

def resample_sales(data: pd.DataFrame, date_column: str, sales_column: str, freq: str) -> pd.Series:
    """Resample sales data based on a specified frequency."""
    if freq == 'W':
        return data.resample('W-SUN', on=date_column)[sales_column].sum()
    elif freq == 'M':
        return data.resample('ME', on=date_column)[sales_column].sum()
    elif freq == 'Q':
        return data.resample('QE-DEC', on=date_column)[sales_column].sum()
    else:
        raise ValueError("Unsupported frequency. Use 'W' for weekly, 'M' for monthly, or 'Q' for quarterly.")

def day_of_week_analysis(data: pd.DataFrame, date_column: str, sales_column: str) -> pd.Series:
    """Analyze sales by day of the week."""
    data['DayOfWeek'] = data[date_column].dt.day_name()
    return data.groupby('DayOfWeek')[sales_column].sum().sort_values()

def time_of_day_analysis(data: pd.DataFrame, time_column: str, sales_column: str) -> pd.Series:
    """Analyze sales by time of the day."""
    # Strip whitespace and map time of day to labels
    data[time_column] = data[time_column].str.strip()
    data['TimeOfDay'] = data[time_column]
    
    # Debugging: Print the 'TimeOfDay' column to verify the mapping
    print("Mapped TimeOfDay column:\n", data[['TimeOfDay', time_column]].head())

    # Group by 'TimeOfDay' and sum sales
    grouped_sales = data.groupby('TimeOfDay')[sales_column].sum().sort_values()
    
    # Debugging: Print the grouped sales data
    print("Grouped Sales by TimeOfDay:\n", grouped_sales)
    
    return grouped_sales

def correlation_analysis(data: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Analyze correlation between specified columns."""
    return data[columns].corr()
