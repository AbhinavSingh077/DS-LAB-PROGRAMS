import pandas as pd

# ==========================================
# EXERCISE 1: IMPORT CSV AND EXCEL DATASETS
# ==========================================

# Import CSV dataset
csv_data = pd.read_csv("Exercise_1/data/students.csv")

print("========== CSV DATA ==========")
print(csv_data)

# Dataset information
print("\n========== DATASET INFORMATION ==========")
csv_data.info()

# Data types
print("\n========== DATA TYPES ==========")
print(csv_data.dtypes)

# Summary statistics
print("\n========== SUMMARY STATISTICS ==========")
print(csv_data.describe())

# ==========================================
# CREATE EXCEL FILE
# ==========================================

csv_data.to_excel("Exercise_1/data/students.xlsx", index=False)

print("\nExcel file created successfully!")

# ==========================================
# IMPORT EXCEL DATASET
# ==========================================

excel_data = pd.read_excel("Exercise_1/data/students.xlsx")

print("\n========== EXCEL DATA ==========")
print(excel_data)

print("\n========== EXCEL DATA TYPES ==========")
print(excel_data.dtypes)

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
   Data that does not follow a strict table format
   but contains tags or keys.
   Examples: JSON, XML, HTML.

3. Unstructured Data:
   Data without a fixed tabular structure.
   Examples: Images, videos, audio, text documents.
""")