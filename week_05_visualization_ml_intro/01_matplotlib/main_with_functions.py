from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def load_and_inspect_coffee_sales():
    df = pd.read_csv(DATA_DIR / "coffee_sales.csv")

    print("Coffee sales preview:")
    print(df.head())

    print("\nColumns:")
    print(df.columns)

    print("\nData types:")
    print(df.dtypes)

    return df


def plot_coffee_sales_line(df):
    x_values = df["day"]
    y_values = df["cups_sold"]

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.plot(x_values, y_values, marker="o")
    ax.set_title("Coffee Cups Sold This Week")
    ax.set_xlabel("Day")
    ax.set_ylabel("Cups Sold")

    fig.tight_layout()
    plt.show()
    plt.close(fig)


def plot_coffee_sales_bar(df):
    x_values = df["day"]
    y_values = df["cups_sold"]

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.bar(x_values, y_values, color="#4C78A8")
    ax.set_title("Coffee Cups Sold by Day")
    ax.set_xlabel("Day")
    ax.set_ylabel("Cups Sold")

    fig.tight_layout()
    plt.show()
    plt.close(fig)


def compare_plots_with_subplots(df):
    x_values = df["day"]
    y_values = df["cups_sold"]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].plot(x_values, y_values, marker="o")
    axes[0].set_title("Line Plot")
    axes[0].set_xlabel("Day")
    axes[0].set_ylabel("Cups Sold")

    axes[1].bar(x_values, y_values, color="#4C78A8")
    axes[1].set_title("Bar Chart")
    axes[1].set_xlabel("Day")
    axes[1].set_ylabel("Cups Sold")

    fig.tight_layout()
    plt.show()
    plt.close(fig)


def show_simple_customization(df):
    x_values = df["day"]
    y_values = df["cups_sold"]

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(
        x_values,
        y_values,
        color="darkgreen",
        linestyle="--",
        linewidth=2.5,
        marker="o",
    )
    ax.set_title("Coffee Cups Sold This Week", fontsize=14)
    ax.set_xlabel("Day", fontsize=11)
    ax.set_ylabel("Cups Sold", fontsize=11)

    fig.tight_layout()
    plt.show()
    plt.close(fig)


def load_and_plot_study_hours():
    # Teacher note:
    # This is the bridge toward machine learning.
    df = pd.read_csv(DATA_DIR / "study_hours.csv")

    print("\nStudy hours preview:")
    print(df.head())

    x_values = df["hours_studied"]
    y_values = df["test_score"]

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.scatter(x_values, y_values, color="#F58518")
    ax.set_title("Study Hours and Test Score")
    ax.set_xlabel("Hours Studied")
    ax.set_ylabel("Test Score")

    fig.tight_layout()
    plt.show()
    plt.close(fig)


def main():
    coffee_df = load_and_inspect_coffee_sales()
    plot_coffee_sales_line(coffee_df)
    plot_coffee_sales_bar(coffee_df)
    compare_plots_with_subplots(coffee_df)
    show_simple_customization(coffee_df)
    load_and_plot_study_hours()


if __name__ == "__main__":
    main()
