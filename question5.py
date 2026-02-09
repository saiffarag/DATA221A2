import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")

# Create the grade_band column
def grade_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(grade_band)

# Create grouped summary table
summary = df.groupby("grade_band").agg(
    num_students=("grade", "count"),
    avg_absences=("absences", "mean"),
    pct_internet=("internet", "mean")
)

# Convert internet mean to percentage
summary["pct_internet"] = summary["pct_internet"] * 100

# Save the table
summary.to_csv("student_bands.csv")
