import pandas as pd

df = pd.read_csv("emails.csv")

print("--- FIRST 5 RECORDS ---")
print(df.head())
print("\n" + "-" * 40 + "\n")

print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print("\n" + "-" * 40 + "\n")

print("--- DATASET INFORMATION ---")
df.info()
print("\n" + "-" * 40 + "\n")

print("--- MISSING VALUES ---")
print(df.isnull().sum())