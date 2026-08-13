import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# ==========================================
# EXERCISE 2: DATA PREPROCESSING
# ==========================================

# Load dataset
df = pd.read_csv("Exercise_2/data/students.csv")

print("========== ORIGINAL DATA ==========")
print(df)


# ==========================================
# 1. HANDLE MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Fill missing numerical values with mean
numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing values after handling:")
print(df.isnull().sum())


# ==========================================
# 2. REMOVE DUPLICATE RECORDS
# ==========================================

print("\n========== DUPLICATES ==========")

print("Number of duplicate records:",
      df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicates after removal:",
      df.duplicated().sum())


# ==========================================
# 3. DETECT OUTLIERS USING IQR
# ==========================================

print("\n========== OUTLIER DETECTION ==========")

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(f"{column}: {len(outliers)} outliers")


# ==========================================
# 4. NORMALIZATION
# ==========================================

print("\n========== NORMALIZATION ==========")

scaler = MinMaxScaler()

df_normalized = df.copy()

df_normalized[numeric_columns] = scaler.fit_transform(
    df[numeric_columns]
)

print(df_normalized.head())


# ==========================================
# 5. STANDARDIZATION
# ==========================================

print("\n========== STANDARDIZATION ==========")

standard_scaler = StandardScaler()

df_standardized = df.copy()

df_standardized[numeric_columns] = standard_scaler.fit_transform(
    df[numeric_columns]
)

print(df_standardized.head())


# ==========================================
# 6. CATEGORICAL VARIABLES TO NUMERICAL
# ==========================================

print("\n========== CATEGORICAL ENCODING ==========")

df_encoded = pd.get_dummies(
    df,
    columns=["Gender", "Department"],
    dtype=int
)

print(df_encoded.head())


# ==========================================
# FINAL DATASET
# ==========================================

print("\n========== FINAL PREPROCESSED DATA ==========")
print(df_encoded)

print("\nData preprocessing completed successfully!")