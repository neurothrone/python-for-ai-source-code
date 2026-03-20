# %%
# Step 1: Observe the input data first

# Step 2: Setup (Import our libraries and load our data into our table, the dataframe)
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path.cwd()
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "coffee_sales.csv")

# %%
# Step 3: Inspect the data
print("Coffee sales preview:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# %%
# Step 4: Visualize (Line Plot)
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

# %%
# Step 4: Visualize (Bar Plot)
x_values = df["day"]
y_values = df["cups_sold"]

fig, ax = plt.subplots(figsize=(7, 4))

ax.bar(x_values, y_values, color="#4C78A8")
ax.set_title("Coffee Cups Sold This Week")
ax.set_xlabel("Day")
ax.set_ylabel("Cups Sold")

fig.tight_layout()
plt.show()
plt.close(fig)

# %%
# Step 4: Visualize (Subplotting)
x_values = df["day"]
y_values = df["cups_sold"]

# [Line Plot][Bar Plot]
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x_values, y_values, marker="o")
axes[0].set_title("Coffee Cups Sold This Week")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Cups Sold")

axes[1].bar(x_values, y_values, color="#4C78A8")
axes[1].set_title("Coffee Cups Sold This Week")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Cups Sold")

fig.tight_layout()
plt.show()
plt.close(fig)

# %%
# Step 4: Visualize (Customization)
x_values = df["day"]
y_values = df["cups_sold"]

fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(
    x_values,
    y_values,
    color="darkgreen",
    linestyle="--",
    linewidth=2.5,
    marker="o"
)
ax.set_title("Coffee Cups Sold This Week", fontsize=14)
ax.set_xlabel("Day", fontsize=11)
ax.set_ylabel("Cups Sold", fontsize=11)

fig.tight_layout()
plt.show()
plt.close(fig)

# %%
# Scatter plot workflow
df = pd.read_csv(DATA_DIR / "study_hours.csv")

print("Study hours preview:")
print(df.head())

x_values = df["hours_studied"]
y_values = df["test_score"]

fig, ax = plt.subplots(figsize=(7, 4))

ax.scatter(x_values, y_values, color="#F58f18")
ax.set_title("Study Hours and Test Score")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Test Score")

fig.tight_layout()
plt.show()
plt.close(fig)
