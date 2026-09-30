import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("data/student_performance.csv")

print("\n===== DATASET INFORMATION =====")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# -----------------------------
# 2. Data Cleaning Checks
# -----------------------------
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== DUPLICATE STUDENT IDs =====")
print(df["Student_ID"].duplicated().sum())

# -----------------------------
# 3. Descriptive Statistics
# -----------------------------
print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe())

# -----------------------------
# 4. Top 5 Students
# -----------------------------
print("\n===== TOP 5 STUDENTS =====")
print(
    df[["Student_ID", "Final_Score"]]
    .sort_values("Final_Score", ascending=False)
    .head(5)
)

# -----------------------------
# 5. Correlation Analysis
# -----------------------------
study_corr = df["Study_Hours"].corr(df["Final_Score"])
attendance_corr = df["Attendance"].corr(df["Final_Score"])

print("\n===== CORRELATION =====")
print("Study Hours vs Final Score:", round(study_corr, 4))
print("Attendance vs Final Score:", round(attendance_corr, 4))

print("\n===== CORRELATION MATRIX =====")
print(df.select_dtypes("number").corr())

# -----------------------------
# 6. Performance Categories
# -----------------------------
df["Performance"] = pd.cut(
    df["Final_Score"],
    bins=[0, 59, 74, 89, 100],
    labels=[
        "Needs Improvement",
        "Average",
        "Good",
        "Excellent"
    ]
)

print("\n===== PERFORMANCE DISTRIBUTION =====")
print(df["Performance"].value_counts())

# -----------------------------
# 7. Create Outputs Folder
# -----------------------------
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# 8. Save Analyzed Dataset
# -----------------------------
df.to_csv(
    "outputs/student_performance_analyzed.csv",
    index=False
)

# -----------------------------
# 9. Study Hours vs Final Score
# -----------------------------
plt.figure()
plt.scatter(df["Study_Hours"], df["Final_Score"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.savefig("outputs/study_hours_vs_final_score.png")
plt.close()

# -----------------------------
# 10. Attendance vs Final Score
# -----------------------------
plt.figure()
plt.scatter(df["Attendance"], df["Final_Score"])
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")
plt.savefig("outputs/attendance_vs_final_score.png")
plt.close()

# -----------------------------
# 11. Midterm vs Final Score
# -----------------------------
plt.figure()
plt.scatter(df["Midterm_Score"], df["Final_Score"])
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")
plt.title("Midterm Score vs Final Score")
plt.savefig("outputs/midterm_vs_final_score.png")
plt.close()

# -----------------------------
# 12. Final Score Distribution
# -----------------------------
plt.figure()
plt.hist(df["Final_Score"], bins=6)
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.title("Final Score Distribution")
plt.savefig("outputs/final_score_distribution.png")
plt.close()

# -----------------------------
# 13. Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8, 6))
correlation = df.select_dtypes("number").corr()

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

print("\n===== ANALYSIS COMPLETED =====")
print("Results saved in the outputs folder.")