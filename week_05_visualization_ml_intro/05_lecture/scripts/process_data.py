from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)

# Read raw data from: DATA_DIR / "music_data_raw.csv"
# Write cleaned data to: OUTPUTS_DIR / "music_data_cleaned.csv"

# Step 1: Load data.
# Example:
# df = pd.read_csv(DATA_DIR / "music_data_raw.csv")

# Step 2: Inspect the data.
# Example:
# print(df.head())
# print(df.columns)
# print(df.isna().sum())

# Step 3: Clean the data.
# Example:
# df = df.drop_duplicates()
# df.to_csv(OUTPUTS_DIR / "music_data_cleaned.csv", index=False)
