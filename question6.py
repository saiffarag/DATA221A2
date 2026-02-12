import pandas as pd

# Load the dataset
df = pd.read_csv("crime.csv")

# Create the risk column
df["risk"] = df["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime"
)

# Group by risk and calculate average unemployment rate
avg_unemployment = df.groupby("risk")["PctUnemployed"].mean()

# Print results
print("Average Unemployment Rate:")
print(f"HighCrime group: {avg_unemployment['HighCrime']}")
print(f"LowCrime group: {avg_unemployment['LowCrime']}")
