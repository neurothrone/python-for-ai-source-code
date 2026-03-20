# %%
# 1. Setup: import libraries and load the data
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path.cwd()
DATA_DIR = BASE_DIR / "data"

# %%
# 2. Inspect the data
df = pd.read_csv(DATA_DIR / "student_scores.csv")

print("Student scores preview:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# %% 3. Visualize student scores dataset with a Scatter Plot
df = pd.read_csv(DATA_DIR / "student_scores.csv")

x_column = "hours_studied"
y_column = "test_score"

fig, ax = plt.subplots(figsize=(7, 4))

sns.scatterplot(data=df, x=x_column, y=y_column, size=80, ax=ax)

ax.set_title("Study Hours and Test Score")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Test Score")

fig.tight_layout()
plt.show()
plt.close(fig)

# %% 3. Visualize Snack Sales dataset with a Bar Plot
df = pd.read_csv(DATA_DIR / "snack_sales.csv")

x_column = "item"
y_column = "units_sold"

fig, ax = plt.subplots(figsize=(7, 4))

sns.lineplot(
    data=df,
    x=x_column,
    y=y_column,
    marker="o",
    color="#E45756",
    ax=ax
)

ax.set_title("Snack Sales")
ax.set_xlabel("Item")
ax.set_ylabel("Units Sold")

fig.tight_layout()
plt.show()
plt.close(fig)

# %% 3. Visualize student scores dataset with a Line Plot
df = pd.read_csv(DATA_DIR / "student_scores.csv")

x_column = "hours_studied"
y_column = "test_score"

fig, ax = plt.subplots(figsize=(7, 4))

sns.lineplot(data=df, x=x_column, y=y_column, marker="o", color="#E45756", ax=ax)

ax.set_title("Score Trend by Study Hours")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Test Score")

fig.tight_layout()
plt.show()
plt.close(fig)

# %% 3. Visualize (Customization)
df = pd.read_csv(DATA_DIR / "student_scores.csv")

x_column = "hours_studied"
y_column = "test_score"

sns.set_theme(style="whitegrid")

fig, ax = plt.subplots(figsize=(8, 4))

sns.lineplot(
    data=df,
    x=x_column,
    y=y_column,
    marker="o",
    color="teal",
    ax=ax
)

ax.set_title("Score Trend by Study Hours")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Test Score")

fig.tight_layout()
plt.show()
plt.close(fig)

# %% 3. Visualize 
df = pd.read_csv(DATA_DIR / "fitness_data.csv")

x_column = "walk_minutes"
y_column = "calories_burned"

fig, ax = plt.subplots(figsize=(7, 4))

# Plot 1
sns.scatterplot(
    data=df,
    x=x_column,
    y=y_column,
    size=80,
    color="purple",
    ax=ax
)

ax.set_title("Walking Time and Calories Burned")
ax.set_xlabel("Walking Minutes")
ax.set_ylabel("Calories Burned")

fig.tight_layout()
plt.show()
plt.close(fig)

# Plot 2
fig, ax = plt.subplots(figsize=(7, 4))

sns.lineplot(
    data=df,
    x=x_column,
    y=y_column,
    marker="o",
    color="darkgreen",
    ax=ax
)

ax.set_title("Calories Burned by Walking Time")
ax.set_xlabel("Walking Minutes")
ax.set_ylabel("Calories Burned")

fig.tight_layout()
plt.show()
plt.close(fig)
