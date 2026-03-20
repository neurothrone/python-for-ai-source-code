from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

BASE_DIR = Path.cwd()
DATA_DIR = BASE_DIR / "data"


def load_data():
    df = pd.read_csv(DATA_DIR / "study_performance.csv")

    print("Study performance preview:")
    print(df.head())

    print("\nColumns:")
    print(df.columns)

    return df


def prepare_feature_and_target(df):
    feature_column = "hours_studied"
    target_column = "test_score"

    X = df[[feature_column]]  # We are using double brackets for X so it stays table-shaped (DataFrame)
    y = df[target_column]  # Series

    print(f"\nFeature type: {type(X)}")
    print(f"Target type: {type(y)}")
    print(f"Feature column: {feature_column}")
    print(f"Target column: {target_column}")

    return X, y, feature_column, target_column


def train_and_predict(X, y, feature_column):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nTest input values:")
    print(X_test)

    print("\nPredicted values:")
    print(predictions)

    print("\nActual values:")
    print(y_test.values)

    results_df = X_test.copy()
    results_df["actual_score"] = y_test.values
    results_df["predicted_score"] = predictions

    print("\nComparison table:")
    print(results_df)

    new_data = pd.DataFrame({feature_column: [9]})
    new_prediction = model.predict(new_data)
    print(f"\nPredicted score for 9 study hours: {new_prediction[0]}")


def main():
    df = load_data()
    X, y, feature_column, _ = prepare_feature_and_target(df)
    train_and_predict(X, y, feature_column)


if __name__ == "__main__":
    main()
