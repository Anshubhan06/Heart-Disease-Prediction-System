import pandas as pd

# Read dataset
df = pd.read_csv("dataset/Heart_Disease_Prediction.csv")

print("========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== SHAPE ==========\n")
print(df.shape)

print("\n========== COLUMNS ==========\n")
print(df.columns)

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

print("\n========== DATA TYPES ==========\n")
print(df.dtypes)

print("\n========== TARGET COLUMN ==========\n")
print(df["Heart Disease"].value_counts())