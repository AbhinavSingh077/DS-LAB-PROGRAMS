import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# EXERCISE 4: EXPLORATORY DATA ANALYSIS
# ==========================================

# Load dataset
df = pd.read_csv("Exercise_4/data/students.csv")

print("========== DATASET ==========")
print(df)

# ==========================================
# 1. BASIC INFORMATION
# ==========================================

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== SHAPE ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ==========================================
# 2. CORRELATION MATRIX
# ==========================================

numeric_data = df.select_dtypes(include=np.number)

correlation_matrix = numeric_data.corr()

print("\n========== CORRELATION MATRIX ==========")
print(correlation_matrix)


# ==========================================
# 3. COVARIANCE MATRIX
# ==========================================

covariance_matrix = numeric_data.cov()

print("\n========== COVARIANCE MATRIX ==========")
print(covariance_matrix)


# ==========================================
# 4. CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# ==========================================
# 5. DETECT OUTLIERS
# ==========================================

print("\n========== OUTLIER DETECTION ==========")

for column in numeric_data.columns:

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
# 6. STUDENT PERFORMANCE TREND
# ==========================================

df["Average_Marks"] = df[
    ["Maths", "Python", "Database"]
].mean(axis=1)

print("\n========== STUDENT PERFORMANCE ==========")

print(
    df[
        ["Name", "Maths", "Python", "Database", "Average_Marks"]
    ]
)


# ==========================================
# 7. HIGHEST PERFORMER
# ==========================================

highest_student = df.loc[
    df["Average_Marks"].idxmax()
]

print("\n========== HIGHEST PERFORMER ==========")

print("Name:", highest_student["Name"])
print("Average Marks:", highest_student["Average_Marks"])


# ==========================================
# 8. LOWEST PERFORMER
# ==========================================

lowest_student = df.loc[
    df["Average_Marks"].idxmin()
]

print("\n========== LOWEST PERFORMER ==========")

print("Name:", lowest_student["Name"])
print("Average Marks:", lowest_student["Average_Marks"])


# ==========================================
# 9. DEPARTMENT-WISE PERFORMANCE
# ==========================================

department_performance = df.groupby(
    "Department"
)["Average_Marks"].mean()

print("\n========== DEPARTMENT-WISE PERFORMANCE ==========")

print(department_performance)


# ==========================================
# 10. ATTENDANCE AND MARKS RELATIONSHIP
# ==========================================

attendance_correlation = df[
    "Attendance"
].corr(df["Average_Marks"])

print("\n========== ATTENDANCE VS MARKS ==========")

print(
    "Correlation between Attendance and Average Marks:",
    attendance_correlation
)


# ==========================================
# 11. SCATTER PLOT
# ==========================================

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="Attendance",
    y="Average_Marks"
)

plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.show()


# ==========================================
# 12. BOX PLOT
# ==========================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=numeric_data
)

plt.title("Box Plot of Numerical Variables")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ==========================================
# EDA CONCLUSION
# ==========================================

print("\n========== EDA CONCLUSION ==========")

print("""
1. Correlation shows the strength of relationships
   between numerical variables.

2. Covariance shows how two variables change together.

3. The heatmap makes strong and weak relationships
   easier to identify.

4. IQR method is used to detect outliers.

5. Average marks help identify student performance.

6. Department-wise analysis helps compare departments.

7. Attendance can be compared with marks to understand
   whether attendance is related to academic performance.
""")

print("\nExploratory Data Analysis completed successfully!")