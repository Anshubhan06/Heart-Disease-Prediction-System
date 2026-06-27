# ==========================================
# AI Healthcare Project
# Heart Disease Prediction Model
# ==========================================

# Import Libraries
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ------------------------------------------
# Step 1 : Load Dataset
# ------------------------------------------

df = pd.read_csv("dataset/Heart_Disease_Prediction.csv")

print("Dataset Loaded Successfully!\n")

# ------------------------------------------
# Step 2 : Label Encoding
# ------------------------------------------

df["Heart Disease"] = df["Heart Disease"].map({
    "Presence": 1,
    "Absence": 0
})

print("Target Column Encoded!\n")

# ------------------------------------------
# Step 3 : Features (X) and Target (y)
# ------------------------------------------

X = df.drop("Heart Disease", axis=1)

y = df["Heart Disease"]

print("Features and Target Created!\n")

# ------------------------------------------
# Step 4 : Split Dataset
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Dataset Split Completed!\n")

# ------------------------------------------
# Step 5 : Train Random Forest
# ------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Trained Successfully!\n")

# ------------------------------------------
# Step 6 : Predictions
# ------------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------------
# Step 7 : Accuracy
# ------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy : {accuracy * 100:.2f}%\n")

# ------------------------------------------
# Step 8 : Save Model
# ------------------------------------------

joblib.dump(model, "model/heart_disease_model.pkl")

print("Model Saved Successfully!")