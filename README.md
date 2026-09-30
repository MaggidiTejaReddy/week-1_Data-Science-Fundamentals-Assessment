# Student Performance Analysis

## Week 1 - Data Science Fundamentals Assessment

### Objective

The objective of this project is to analyze student performance data using Python and Pandas. The analysis examines study hours, attendance, assignment scores, midterm scores, and final scores.

## Dataset

The dataset contains performance information for 20 students.

### Features

- Student_ID
- Gender
- Age
- Study_Hours
- Attendance
- Assignments_Score
- Midterm_Score
- Final_Score

## Data Cleaning

The dataset was checked for:

- Missing values
- Duplicate records
- Duplicate Student IDs
- Data types

### Results

- Missing values: 0
- Duplicate rows: 0
- Duplicate Student IDs: 0

Therefore, no major data-cleaning operations were required.

## Exploratory Data Analysis

The following analyses were performed:

1. Top 5 students based on Final Score
2. Study Hours vs Final Score
3. Attendance vs Final Score
4. Midterm Score vs Final Score
5. Final Score distribution
6. Correlation analysis
7. Performance categorization

## Key Statistics

| Metric | Value |
|---|---:|
| Number of Students | 20 |
| Average Study Hours | 3.85 |
| Average Attendance | 81.70% |
| Average Assignment Score | 78.40 |
| Average Midterm Score | 75.25 |
| Average Final Score | 77.85 |
| Highest Final Score | 95 |
| Lowest Final Score | 50 |

## Correlation Analysis

| Variables | Correlation |
|---|---:|
| Study Hours vs Final Score | 0.9772 |
| Attendance vs Final Score | 0.9854 |

The results indicate very strong positive linear associations within this dataset. Correlation does not by itself establish causation.

## Performance Categories

- Excellent: 4 students
- Good: 10 students
- Average: 5 students
- Needs Improvement: 1 student

## Visualizations

The project includes the following visualizations:

- Study Hours vs Final Score
- Attendance vs Final Score
- Midterm Score vs Final Score
- Final Score Distribution
- Correlation Heatmap

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- PowerShell
- VS Code

## Conclusion

The analysis demonstrates how Python-based data science techniques can be used to clean, explore, analyze, and visualize student performance data. The dataset shows strong positive associations between study hours, attendance, and final scores. Further analysis with a larger and more diverse dataset would be required for broader conclusions.