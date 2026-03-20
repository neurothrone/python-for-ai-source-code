# %% Step 1. Import and load data
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

BASE_DIR = Path.cwd()
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

df = pd.read_csv(DATA_DIR / "tutoring_data.csv")

# %% Step 2. Inspect data
print("Tutoring data preview:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# %% Step 3. Create Scatter Plot
OUTPUT_DIR.mkdir(exist_ok=True)

plot_file_path = OUTPUT_DIR / "tutoring_scatter.png"

x_column = "hours_with_tutor"
y_column = "test_score"

fig, ax = plt.subplots(figsize=(7, 4))

sns.scatterplot(data=df, x=x_column, y=y_column, size=80, ax=ax)

ax.set_title("Tutor Hours and Test Score")
ax.set_xlabel("Hours with Tutor")
ax.set_ylabel("Test Score")

fig.tight_layout()
fig.savefig(plot_file_path, dpi=150)

plt.show()
plt.close(fig)

print(f"Saved plot at: {plot_file_path}")

# %% Step 4: Train a model/Build a results table/Save the results file
feature_column = "hours_with_tutor"
target_column = "test_score"

X = df[[feature_column]]  # We are using double brackets for X so it stays table-shaped (DataFrame)
y = df[target_column] # Series

print(f"Feature column: {feature_column}")
print(f"Target column: {target_column}")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.29,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

results_df = X_test.copy()
results_df["actual_score"] = y_test.values
results_df["predicted_score"] = predictions

print("Reults table:")
print(results_df)

results_path = OUTPUT_DIR / "tutoring_predictions.csv"
results_df.to_csv(results_path, index=False)
print(f"Saved prediciton results at: {results_path}")
