# %%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "study_hours.csv")

x_column = "hours_studied"
y_column = "test_score"

fig, ax = plt.subplots()

# With Seaborn, data= tells the function which DataFrame to use.
# x= and y= tell it which column names to plot.
sns.lineplot(data=df, x=x_column, y=y_column, ax=ax)

ax.set_title("Study Hours and Test Score")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Test Score")

plt.show()
plt.close(fig)

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "coffee_sales.csv")

x_column = "day"
y_column = "cups_sold"

fig, ax = plt.subplots()

# Seaborn also uses Matplotlib under the hood.
# ax=ax tells Seaborn which chart area to draw on.
sns.barplot(data=df, x=x_column, y=y_column, ax=ax)

ax.set_title("Coffee Cups Sold This Week")
ax.set_xlabel("Day")
ax.set_ylabel("Cups Sold")

plt.show()
plt.close(fig)
# %%
