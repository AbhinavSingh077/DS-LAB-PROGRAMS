import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# EXERCISE 5: DATA VISUALIZATION
# ==========================================

# Load dataset
df = pd.read_csv("Exercise_5/data/students.csv")

# Calculate average marks
df["Average_Marks"] = df[
    ["Maths", "Python", "Database"]
].mean(axis=1)


# ==========================================
# 1. HISTOGRAM
# ==========================================

plt.figure(figsize=(8, 6))

plt.hist(
    df["Maths"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribution of Maths Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()


# Interpretation:
print("""
HISTOGRAM INTERPRETATION:
The histogram shows the distribution of Maths marks.
It helps identify how the students' marks are distributed
across different score ranges.
""")


# ==========================================
# 2. BAR CHART
# ==========================================

department_average = df.groupby(
    "Department"
)["Average_Marks"].mean()

plt.figure(figsize=(8, 6))

plt.bar(
    department_average.index,
    department_average.values
)

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.show()


print("""
BAR CHART INTERPRETATION:
The bar chart compares the average marks of students
from different departments. The tallest bar represents
the department with the highest average performance.
""")


# ==========================================
# 3. LINE CHART
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    df["Student_ID"],
    df["Average_Marks"],
    marker="o"
)

plt.title("Student Performance Trend")
plt.xlabel("Student ID")
plt.ylabel("Average Marks")

plt.grid(True)

plt.tight_layout()
plt.show()


print("""
LINE CHART INTERPRETATION:
The line chart shows how average student performance
changes across the student IDs. It helps identify
increases and decreases in performance.
""")


# ==========================================
# 4. PIE CHART
# ==========================================

gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    gender_counts.values,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

plt.tight_layout()
plt.show()


print("""
PIE CHART INTERPRETATION:
The pie chart shows the proportion of male and female
students in the dataset.
""")


# ==========================================
# 5. SCATTER PLOT
# ==========================================

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="Attendance",
    y="Average_Marks"
)

plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.show()


print("""
SCATTER PLOT INTERPRETATION:
The scatter plot shows the relationship between attendance
and average marks. It helps determine whether students
with higher attendance tend to achieve higher marks.
""")


# ==========================================
# 6. BOX PLOT
# ==========================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df[
        ["Maths", "Python", "Database"]
    ]
)

plt.title("Distribution of Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()


print("""
BOX PLOT INTERPRETATION:
The box plot shows the distribution, median, quartiles,
and possible outliers for Maths, Python, and Database marks.
""")


print("\n==========================================")
print("ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("==========================================")