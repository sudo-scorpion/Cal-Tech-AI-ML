import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_sales_trends(
    data: pd.DataFrame,
    group_column: str,
    date_column: str,
    sales_column: str,
    title: str,
) -> None:
    """Plot sales trends over time for specified groups."""
    sns.set(style="whitegrid")

    # Aggregate data by month-end
    data_aggregated = (
        data.groupby([group_column, pd.Grouper(key=date_column, freq="ME")])[
            sales_column
        ]
        .sum()
        .reset_index()
    )

    unique_groups = data_aggregated[group_column].unique()

    plt.figure(figsize=(10, 6))  # Smaller size
    for group in unique_groups:
        group_data = data_aggregated[data_aggregated[group_column] == group]
        plt.plot(
            group_data[date_column], group_data[sales_column], marker="o", label=group
        )

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend(title=group_column)
    plt.grid(True)
    plt.show()


def plot_day_of_week_sales(data: pd.Series, title: str) -> None:
    """Plot sales by day of the week."""
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))  # Smaller size
    ax = sns.barplot(x=data.index, y=data.values)
    ax.set_title(title)
    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Sales")

    # Add data labels
    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.0f}",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
        )

    plt.show()


def plot_time_of_day_sales(data: pd.Series, title: str) -> None:
    """Plot sales by time of the day."""
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))  # Smaller size
    ax = sns.barplot(x=data.index, y=data.values)
    ax.set_title(title)
    ax.set_xlabel("Time of the Day")
    ax.set_ylabel("Sales")

    # Add data labels
    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.0f}",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
        )

    plt.show()


def plot_correlation_heatmap(data: pd.DataFrame, title: str) -> None:
    """Plot correlation heatmap."""
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))  # Smaller size
    sns.heatmap(data, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title(title)
    plt.show()


def plot_monthly_sales_trends(
    data: pd.DataFrame, date_column: str, sales_column: str, title: str
) -> None:
    """Plot detailed monthly sales trends."""
    sns.set(style="whitegrid")

    # Aggregate data by month-end
    data["Month"] = data[date_column].dt.to_period("M")
    monthly_sales = data.groupby("Month")[sales_column].sum().reset_index()
    monthly_sales["Month"] = monthly_sales["Month"].dt.to_timestamp()

    plt.figure(figsize=(10, 6))  # Smaller size
    ax = sns.lineplot(
        x=monthly_sales["Month"], y=monthly_sales[sales_column], marker="o"
    )
    ax.set_title(title)
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")

    # Add data labels
    for x, y in zip(monthly_sales["Month"], monthly_sales[sales_column]):
        ax.annotate(
            f"{y:.0f}",
            xy=(x, y),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center",
        )

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def plot_yearly_sales_trends(
    data: pd.DataFrame, date_column: str, sales_column: str, title: str
) -> None:
    """Plot yearly sales trends."""
    sns.set(style="whitegrid")

    # Aggregate data by year
    data["Year"] = data[date_column].dt.to_period("Y")
    yearly_sales = data.groupby("Year")[sales_column].sum().reset_index()
    yearly_sales["Year"] = yearly_sales["Year"].dt.to_timestamp()

    plt.figure(figsize=(10, 6))  # Smaller size
    ax = sns.lineplot(x=yearly_sales["Year"], y=yearly_sales[sales_column], marker="o")
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")

    # Add data labels
    for x, y in zip(yearly_sales["Year"], yearly_sales[sales_column]):
        ax.annotate(
            f"{y:.0f}",
            xy=(x, y),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center",
        )

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
