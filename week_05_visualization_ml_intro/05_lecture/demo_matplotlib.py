# %%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

# Common Matplotlib plot types:
# plt.plot() -> line plot
# plt.bar() -> bar chart
# plt.scatter() -> scatter plot

df = pd.read_csv(DATA_DIR / "study_hours.csv")

# Give the x-axis and y-axis data clear names before plotting.
x_values = df["hours_studied"]
y_values = df["test_score"]

# Quick first look:
# plt.plot(x_values, y_values)

# Recommended beginner-friendly pattern:
fig, ax = plt.subplots()  # Create a figure and one set of axes, then draw the chart on those axes.

ax.plot(x_values, y_values)

ax.set_title("Study Hours and Test Score")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Test Score")

plt.show()  # Show the figure. This will open a window with the chart.
plt.close(fig)  # Close the figure after showing it so it does not stay open in memory.

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "coffee_sales.csv")

x_values = df["day"]
y_values = df["cups_sold"]

fig, ax = plt.subplots()

ax.bar(x_values, y_values)

ax.set_title("Coffee Cups Sold This Week")
ax.set_xlabel("Day")
ax.set_ylabel("Cups Sold")

plt.show()
plt.close(fig)
