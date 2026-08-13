import pandas as pd
import numpy as np

# ==========================================
# EXERCISE 3: DESCRIPTIVE STATISTICS
# ==========================================

# Load dataset
df = pd.read_csv("Exercise_3/data/students.csv")

print("========== DATASET ==========")
print(df)

# Select numerical columns
numeric_data = df.select_dtypes(include=np.number)

print("\n========== NUMERICAL DATA ==========")
print(numeric_data)

# ==========================================
# 1. MEAN
# ==========================================

print("\n========== MEAN ==========")
print(numeric_data.mean())

# ==========================================
# 2. MEDIAN
# ==========================================

print("\n========== MEDIAN ==========")
print(numeric_data.median())

# ==========================================
# 3. MODE
# ==========================================

print("\n========== MODE ==========")
print(numeric_data.mode().iloc[0])

# ==========================================
# 4. VARIANCE
# ==========================================

print("\n========== VARIANCE ==========")
print(numeric_data.var())

# ==========================================
# 5. STANDARD DEVIATION
# ==========================================

print("\n========== STANDARD DEVIATION ==========")
print(numeric_data.std())

# ==========================================
# 6. QUARTILES
# ==========================================

print("\n========== QUARTILES ==========")

print("25th Percentile (Q1):")
print(numeric_data.quantile(0.25))

print("\n50th Percentile (Q2 / Median):")
print(numeric_data.quantile(0.50))

print("\n75th Percentile (Q3):")
print(numeric_data.quantile(0.75))

# ==========================================
# 7. PERCENTILES
# ==========================================

print("\n========== PERCENTILES ==========")

print("10th Percentile:")
print(numeric_data.quantile(0.10))

print("\n25th Percentile:")
print(numeric_data.quantile(0.25))

print("\n50th Percentile:")
print(numeric_data.quantile(0.50))

print("\n75th Percentile:")
print(numeric_data.quantile(0.75))

print("\n90th Percentile:")
print(numeric_data.quantile(0.90))

# ==========================================
# 8. COMPLETE STATISTICAL SUMMARY
# ==========================================

print("\n========== COMPLETE STATISTICAL SUMMARY ==========")
print(numeric_data.describe())

print("\nDescriptive statistics calculated successfully!")