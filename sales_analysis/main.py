import pandas as pd
from data_wrangling import (
    load_data,
    inspect_data,
    clean_data,
    normalize_columns,
    remove_outliers,
    convert_to_datetime,
)
from data_analysis import (
    descriptive_statistics,
    group_sales_statistics,
    resample_sales,
    day_of_week_analysis,
    time_of_day_analysis,
    correlation_analysis,
)
from data_visualization import (
    plot_sales_trends,
    plot_day_of_week_sales,
    plot_time_of_day_sales,
    plot_correlation_heatmap,
    plot_monthly_sales_trends,
    plot_yearly_sales_trends,
)


def main() -> None:
    # Load the data
    filepath = "/home/saif/Desktop/caltech/AusApparalSales4thQrt2020.csv"
    data = load_data(filepath)

    # Inspect the data
    inspect_data(data)

    # Data Wrangling
    data_cleaned = clean_data(data)
    data_cleaned = normalize_columns(data_cleaned, ["Sales", "Unit"])
    data_cleaned = remove_outliers(data_cleaned, ["Sales", "Unit"])
    data_cleaned = convert_to_datetime(data_cleaned, "Date")

    # Descriptive Statistical Analysis
    sales_stats = descriptive_statistics(data_cleaned, "Sales")
    unit_stats = descriptive_statistics(data_cleaned, "Unit")
    print("Sales descriptive statistics:\n", sales_stats)
    print("Unit descriptive statistics:\n", unit_stats)

    highest_sales_group, lowest_sales_group = group_sales_statistics(
        data_cleaned, "Group", "Sales"
    )
    print("Group with highest sales:", highest_sales_group)
    print("Group with lowest sales:", lowest_sales_group)

    # Generate weekly, monthly, and quarterly reports
    weekly_sales = resample_sales(data_cleaned, "Date", "Sales", "W")
    monthly_sales = resample_sales(data_cleaned, "Date", "Sales", "M")
    quarterly_sales = resample_sales(data_cleaned, "Date", "Sales", "Q")
    print("Weekly Sales:\n", weekly_sales)
    print("Monthly Sales:\n", monthly_sales)
    print("Quarterly Sales:\n", quarterly_sales)

    # Additional Analyses
    day_of_week_sales = day_of_week_analysis(data_cleaned, "Date", "Sales")
    print("Day of the Week Sales:\n", day_of_week_sales)

    time_of_day_sales = time_of_day_analysis(data_cleaned, "Time", "Sales")
    print("Time of the Day Sales:\n", time_of_day_sales)

    correlation_matrix = correlation_analysis(data_cleaned, ["Sales", "Unit"])
    print("Correlation Analysis:\n", correlation_matrix)

    # Visualize the Data
    plot_sales_trends(
        data_cleaned, "State", "Date", "Sales", "State-wise Sales Trends Over Time"
    )
    plot_sales_trends(
        data_cleaned,
        "Group",
        "Date",
        "Sales",
        "Demographic Group-wise Sales Trends Over Time",
    )
    plot_day_of_week_sales(day_of_week_sales, "Sales by Day of the Week")
    plot_time_of_day_sales(time_of_day_sales, "Sales by Time of the Day")
    plot_correlation_heatmap(
        correlation_matrix, "Correlation Heatmap of Sales and Units"
    )
    plot_monthly_sales_trends(
        data_cleaned, "Date", "Sales", "Detailed Monthly Sales Trends"
    )
    plot_yearly_sales_trends(data_cleaned, "Date", "Sales", "Yearly Sales Trends")

    # Recommendations
    print("Recommendations based on analysis:")
    print(
        f"The group with the highest sales is {highest_sales_group}, and the group with the lowest sales is {lowest_sales_group}."
    )
    print(
        "State-wise and demographic-wise sales trends should be considered for strategic planning."
    )
    print("Invest in high-performing states and develop tailored marketing campaigns.")
    print(
        "Implement targeted sales programs and localized marketing efforts in low-performing states."
    )
    print(
        "Focus on demographic groups with lower sales to understand and address their unique needs."
    )
    print(
        "Optimize staffing and promotional activities based on day-of-the-week and time-of-day sales trends."
    )
    print(
        "Utilize correlation analysis to better understand relationships between units sold and revenue."
    )


if __name__ == "__main__":
    main()
