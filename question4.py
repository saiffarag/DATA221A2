import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")

# Filter students:
# studytime ≥ 3, internet = 1, absences ≤ 5
filtered = df[
    (df["studytime"] >= 3) &
    (df["internet"] == 1) &
    (df["absences"] <= 5)
]

# Save filtered data
filtered.to_csv("high_engagement.csv", index=False)

# Compute required statistics
num_students = len(filtered)
avg_grade = filtered["grade"].mean()

# Print results
print(num_students)
print(avg_grade)
