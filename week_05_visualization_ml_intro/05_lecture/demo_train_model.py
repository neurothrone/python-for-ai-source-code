from pathlib import Path

# Step 0: Install and import libraries.
# `pip install pandas scikit-learn joblib`
# `pip freeze > requirements.txt`

# This example predicts a category (`genre`), so it uses classification.
# It is a simple machine learning demo, not a linear regression example.

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

MODELS_DIR.mkdir(exist_ok=True)

# Step 1: Load the dataset.
df = pd.read_csv(DATA_DIR / "music_data_raw.csv")

# Optional: inspect the first rows.
# print(df.head())

# Step 2: Clean data if needed.
# This small demo dataset is already clean, so we do not change anything here.
# ...

# --- The regular data workflow above ---
# --- The machine learning workflow starts here ---

# Step 3: Choose input columns (features) and the output column (target).
feature_columns = ["age", "gender"]
target_column = "genre"

X = df[feature_columns]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,  # 75% training and 25% test
    # NOTE: Keep results reproducible by setting a random seed.
    # You can use any number here, but using the same number
    # will give you the same results.
    # random_state=42,
)

# Step 4: Create the model.
model = DecisionTreeClassifier()

# Step 5: Train the model with the training data.
model.fit(X_train, y_train)

# Step 6: Make predictions for the test rows.
predictions = model.predict(X_test)

# Put the input rows, real answers, and predictions side by side.
results_df = X_test.copy()
results_df["actual_genre"] = y_test.values
results_df["predicted_genre"] = predictions

print(results_df)

# Step 7: Check model performance in one simple way.
score = accuracy_score(y_test, predictions)
print(f"Accuracy score: {score}")

# Step 8: Save the trained model so it can be used later.
joblib.dump(model, MODELS_DIR / "music_model.joblib")
