import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

DATA_FILE = "data/sample_student_scores.csv"     # <--- Your uploaded file

# ======================================================
# TASK 1: LOAD & CLEAN DATA
# ======================================================

try:
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    print("❌ ERROR: sample_student_scores.csv not found.")
    exit()

print("\n=== RAW DATA HEAD ===")
print(df.head())

# Convert column names to lowercase for safety
df.columns = df.columns.str.lower()

required_cols = ["name", "roll_no", "gender", "subject", "marks", "attendance"]

missing = [c for c in required_cols if c not in df.columns]
if missing:
    print("❌ Missing required columns:", missing)
    exit()

# Convert to numeric
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce")

# Drop rows with missing values
df = df.dropna()

# Validate marks range
df = df[(df["marks"] >= 0) & (df["marks"] <= 100)]

df_students = df.copy()
print("\n=== CLEANED DATA ===")
print(df_students.head())

# ======================================================
# TASK 2: ANALYSIS
# ======================================================

# Average marks per student
avg_marks = df_students.groupby("name")["marks"].mean()

# Highest/lowest marks per subject
subject_stats = df_students.groupby("subject")["marks"].agg(["min", "max", "mean"])

# Standard deviation
marks_std = np.std(df_students["marks"])

# Top 3 / Bottom 3 performers
top3 = avg_marks.sort_values(ascending=False).head(3)
bottom3 = avg_marks.sort_values().head(3)

# Grades
def grade(m):
    if m >= 90: return "A"
    elif m >= 75: return "B"
    elif m >= 50: return "C"
    else: return "Fail"

df_students["grade"] = df_students["marks"].apply(grade)

print("\n=== STUDENT GRADES ===")
print(df_students[["name", "marks", "grade"]].head())

# ======================================================
# TASK 3: OOP IMPLEMENTATION
# ======================================================

class Student:
    def __init__(self, name, roll_no, gender):
        self.name = name
        self.roll_no = roll_no
        self.gender = gender
        self.marks = []  # list of (subject, marks)

    def add_marks(self, subject, marks):
        self.marks.append((subject, marks))

    def average(self):
        return sum(m for _, m in self.marks) / len(self.marks)

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student_record(self, row):
        key = row["name"]
        if key not in self.students:
            self.students[key] = Student(row["name"], row["roll_no"], row["gender"])
        self.students[key].add_marks(row["subject"], row["marks"])

    def export_report(self, filename):
        with open(filename, "w") as f:
            f.write("Performance Summary Report\n")
            f.write("============================\n\n")
            f.write(f"Top 3 Performers:\n{top3}\n\n")
            f.write(f"Lowest Avg Subject:\n{subject_stats['mean'].idxmin()}\n\n")
            f.write(f"Class Average Marks: {avg_marks.mean():.2f}\n")

manager = StudentManager()
for _, row in df_students.iterrows():
    manager.add_student_record(row)

# ======================================================
# TASK 4: VISUALIZATIONS
# ======================================================

# Average marks per student (Bar)
bar_data = avg_marks

# Pie Chart — Grade distribution
grade_counts = df_students["grade"].value_counts()

# Subject-wise line chart
subject_avg = df_students.groupby("subject")["marks"].mean()

# Attendance vs Marks – Scatter
att = df_students["attendance"]
mrk = df_students["marks"]

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Bar Chart
axs[0, 0].bar(bar_data.index, bar_data.values)
axs[0, 0].set_title("Average Marks by Student")
axs[0, 0].tick_params(axis='x', rotation=45)

# Pie Chart
axs[0, 1].pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
axs[0, 1].set_title("Grade Distribution")

# Line Chart
axs[1, 0].plot(subject_avg.index, subject_avg.values, marker="o")
axs[1, 0].set_title("Subject-wise Average Marks")
axs[1, 0].set_ylabel("Average Marks")

# Scatter Plot
axs[1, 1].scatter(att, mrk)
axs[1, 1].set_title("Attendance vs Marks")
axs[1, 1].set_xlabel("Attendance")
axs[1, 1].set_ylabel("Marks")

plt.tight_layout()
plt.savefig("student_performance_dashboard.png")
plt.close()

print("\nSaved: student_performance_dashboard.png")

# ======================================================
# TASK 5: SAVE CLEANED DATA + REPORT
# ======================================================

os.makedirs("output", exist_ok=True)

df_students.to_csv("output/cleaned_student_data.csv", index=False)

manager.export_report("output/performance_summary.txt")

print("\nSaved:")
print(" output/cleaned_student_data.csv")
print(" output/performance_summary.txt")
print("\nAssignment 5 Completed Successfully!")