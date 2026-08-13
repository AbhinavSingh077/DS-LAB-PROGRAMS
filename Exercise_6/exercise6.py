import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# ==========================================
# EXERCISE 6: INTERACTIVE DASHBOARD
# ==========================================

# Load dataset
df = pd.read_csv("Exercise_6/data/students.csv")

# Calculate average marks
df["Average_Marks"] = df[
    ["Maths", "Python", "Database"]
].mean(axis=1)

# ==========================================
# 1. DEPARTMENT PERFORMANCE
# ==========================================

department_data = df.groupby(
    "Department",
    as_index=False
)["Average_Marks"].mean()

fig1 = px.bar(
    department_data,
    x="Department",
    y="Average_Marks",
    title="Average Marks by Department",
    text_auto=".2f"
)

fig1.update_layout(
    xaxis_title="Department",
    yaxis_title="Average Marks"
)


# ==========================================
# 2. SUBJECT PERFORMANCE
# ==========================================

subject_data = pd.DataFrame({
    "Subject": ["Maths", "Python", "Database"],
    "Average Marks": [
        df["Maths"].mean(),
        df["Python"].mean(),
        df["Database"].mean()
    ]
})

fig2 = px.bar(
    subject_data,
    x="Subject",
    y="Average Marks",
    title="Average Marks by Subject",
    text_auto=".2f"
)


# ==========================================
# 3. ATTENDANCE VS PERFORMANCE
# ==========================================

fig3 = px.scatter(
    df,
    x="Attendance",
    y="Average_Marks",
    color="Department",
    hover_name="Name",
    size="Average_Marks",
    title="Attendance vs Average Marks",
    labels={
        "Attendance": "Attendance (%)",
        "Average_Marks": "Average Marks"
    }
)


# ==========================================
# 4. GENDER DISTRIBUTION
# ==========================================

gender_data = df["Gender"].value_counts().reset_index()

gender_data.columns = ["Gender", "Count"]

fig4 = px.pie(
    gender_data,
    names="Gender",
    values="Count",
    title="Gender Distribution"
)


# ==========================================
# 5. STUDENT PERFORMANCE
# ==========================================

fig5 = px.line(
    df,
    x="Student_ID",
    y="Average_Marks",
    markers=True,
    hover_name="Name",
    title="Student Performance Trend"
)

fig5.update_layout(
    xaxis_title="Student ID",
    yaxis_title="Average Marks"
)


# ==========================================
# 6. CREATE DASHBOARD
# ==========================================

dashboard = make_subplots(
    rows=3,
    cols=2,
    subplot_titles=(
        "Department Performance",
        "Subject Performance",
        "Attendance vs Average Marks",
        "Gender Distribution",
        "Student Performance Trend",
        "Performance Summary"
    ),
    specs=[
        [{"type": "bar"}, {"type": "bar"}],
        [{"type": "scatter"}, {"type": "pie"}],
        [{"type": "scatter"}, {"type": "indicator"}]
    ]
)


# Add Department Bar Chart
for trace in fig1.data:
    dashboard.add_trace(
        trace,
        row=1,
        col=1
    )


# Add Subject Bar Chart
for trace in fig2.data:
    dashboard.add_trace(
        trace,
        row=1,
        col=2
    )


# Add Scatter Plot
for trace in fig3.data:
    dashboard.add_trace(
        trace,
        row=2,
        col=1
    )


# Add Pie Chart
for trace in fig4.data:
    dashboard.add_trace(
        trace,
        row=2,
        col=2
    )


# Add Line Chart
for trace in fig5.data:
    dashboard.add_trace(
        trace,
        row=3,
        col=1
    )


# ==========================================
# PERFORMANCE INDICATOR
# ==========================================

overall_average = df["Average_Marks"].mean()

dashboard.add_trace(
    go.Indicator(
        mode="number",
        value=overall_average,
        title={
            "text": "Overall Average Marks"
        },
        number={
            "valueformat": ".2f"
        }
    ),
    row=3,
    col=2
)


# ==========================================
# DASHBOARD LAYOUT
# ==========================================

dashboard.update_layout(
    title_text="Student Performance Interactive Dashboard",
    height=1000,
    width=1200,
    showlegend=True
)

dashboard.update_xaxes(
    title_text="Department",
    row=1,
    col=1
)

dashboard.update_yaxes(
    title_text="Average Marks",
    row=1,
    col=1
)

dashboard.update_xaxes(
    title_text="Subject",
    row=1,
    col=2
)

dashboard.update_yaxes(
    title_text="Average Marks",
    row=1,
    col=2
)

dashboard.update_xaxes(
    title_text="Attendance (%)",
    row=2,
    col=1
)

dashboard.update_yaxes(
    title_text="Average Marks",
    row=2,
    col=1
)

dashboard.update_xaxes(
    title_text="Student ID",
    row=3,
    col=1
)

dashboard.update_yaxes(
    title_text="Average Marks",
    row=3,
    col=1
)


# ==========================================
# SAVE DASHBOARD
# ==========================================

dashboard.write_html(
    "Exercise_6/student_performance_dashboard.html"
)

print("==========================================")
print("INTERACTIVE DASHBOARD CREATED SUCCESSFULLY")
print("==========================================")

print("\nDashboard saved as:")
print("Exercise_6/student_performance_dashboard.html")

print("\nOverall Average Marks:",
      round(overall_average, 2))

print("\nHighest Performing Student:")

highest_student = df.loc[
    df["Average_Marks"].idxmax()
]

print(highest_student["Name"])
print("Average Marks:",
      round(highest_student["Average_Marks"], 2))

print("\nDashboard contains:")
print("1. Department Performance")
print("2. Subject Performance")
print("3. Attendance vs Marks")
print("4. Gender Distribution")
print("5. Student Performance Trend")
print("6. Overall Average Marks")