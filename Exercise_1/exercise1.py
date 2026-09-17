import pandas as pd
import os

# ==========================================
# EXERCISE 1: IMPORT CSV AND EXCEL DATASETS
# ==========================================

# File paths
csv_file = "Exercise_1/data/students.csv"
excel_file = "Exercise_1/data/students.xlsx"

# ==========================================
# IMPORT CSV DATASET
# ==========================================

csv_data = pd.read_csv(csv_file)

print("========== CSV DATA ==========")
print(csv_data)

# ==========================================
# DATASET INFORMATION
# ==========================================

print("\n========== DATASET INFORMATION ==========")
csv_data.info()

# ==========================================
# DATA TYPES
# ==========================================

print("\n========== DATA TYPES ==========")
print(csv_data.dtypes)

# ==========================================
# SUMMARY STATISTICS
# ==========================================

print("\n========== SUMMARY STATISTICS ==========")
print(csv_data.describe())

# ==========================================
# CREATE EXCEL FILE FROM CSV
# ==========================================

csv_data.to_excel(excel_file, index=False)

print("\nExcel file created successfully!")

# ==========================================
# IMPORT EXCEL DATASET
# ==========================================

excel_data = pd.read_excel(excel_file)

print("\n========== EXCEL DATA ==========")
print(excel_data)

# ==========================================
# EXCEL DATASET INFORMATION
# ==========================================

print("\n========== EXCEL DATASET INFORMATION ==========")
excel_data.info()

# ==========================================
# EXCEL DATA TYPES
# ==========================================

print("\n========== EXCEL DATA TYPES ==========")
print(excel_data.dtypes)

# ==========================================
# EXCEL SUMMARY STATISTICS
# ==========================================

print("\n========== EXCEL SUMMARY STATISTICS ==========")
print(excel_data.describe())

# ==========================================
# TYPES OF DATA
# ==========================================

print("\n========== TYPES OF DATA ==========")

print("""
1. Structured Data:
   Data arranged in rows and columns.
   Examples: CSV files, Excel spreadsheets, SQL tables.

2. Semi-Structured Data:
   Data that does not follow a strict tabular format
   but contains tags or keys.
   Examples: JSON, XML, HTML.

3. Unstructured Data:
   Data without a fixed tabular structure.
   Examples: Images, videos, audio, text documents.
""")

print("========== EXERCISE 1 COMPLETED ==========")