import pandas as pd

# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------
data = pd.read_csv("Census dataset.csv")

# View first rows
print("\n--- Head of Dataset ---")
print(data.head())

# Check shape
print("\nDataset Shape:", data.shape)

# --------------------------------------------------
# 2. Basic Info
# --------------------------------------------------
print("\n--- Dataset Info ---")
print(data.info())

# --------------------------------------------------
# 3. Check Null Values
# --------------------------------------------------
print("\n--- Null Values per Column ---")
print(data.isnull().sum())

# Fill null values with mean (if any)
data_filled = data.fillna(data.mean(numeric_only=True))

# --------------------------------------------------
# 4. Statistical Summary
# --------------------------------------------------
print("\n--- Statistical Description ---")
print(data.describe())

# --------------------------------------------------
# 5. State-wise Population
# --------------------------------------------------
state_population = data.groupby("State_name")["Population"].sum()
print("\n--- State-wise Population ---")
print(state_population)

# --------------------------------------------------
# 6. Religion Distribution (Hindus, Muslims, Christians, Sikhs, Buddhists, Jains)
# --------------------------------------------------
religion_cols = ["Hindus", "Muslims", "Christians", "Sikhs", "Buddhists", "Jains"]
religion_distribution = data[religion_cols].sum()
print("\n--- Total Religious Population in India ---")
print(religion_distribution)

# --------------------------------------------------
# 7. Literacy Analysis
# --------------------------------------------------
if "Literates" in data.columns:
    literacy_rate = (data["Literates"].sum() / data["Population"].sum()) * 100
    print(f"\nOverall Literacy Rate in India: {literacy_rate:.2f}%")

# --------------------------------------------------
# 8. Male vs Female Population
# --------------------------------------------------
if "Male" in data.columns and "Female" in data.columns:
    total_male = data["Male"].sum()
    total_female = data["Female"].sum()

    print(f"\nTotal Male Population: {total_male}")
    print(f"Total Female Population: {total_female}")

# --------------------------------------------------
# 9. Workers Distribution
# --------------------------------------------------
if "Workers" in data.columns:
    total_workers = data["Workers"].sum()
    print(f"\nTotal Workers in India: {total_workers}")

# --------------------------------------------------
# 10. Save Cleaned File
# --------------------------------------------------
data_filled.to_csv("Census_cleaned.csv", index=False)
print("\nCleaned file saved as Census_cleaned.csv")
