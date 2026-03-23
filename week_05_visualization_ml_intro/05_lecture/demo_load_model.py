from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).parent
MODELS_DIR = BASE_DIR / "models"

# Step 1: Load the saved model.
model = joblib.load(MODELS_DIR / "music_model.joblib")

# Step 2: Try the model with one new input row.
# The column names must match the columns used during training.
input_data = pd.DataFrame(
    [[21, 1]],  # 21 years old, male
    columns=["age", "gender"]
)
prediction = model.predict(input_data)

print(f"Predicted music genre: {prediction[0]}")
