import pandas as pd

# 1. Define the raw match data in a dictionary structure
match_data = {
    "Attack_Score": [92, 88, 85, 82, 81, 75, 90, 87, 84, 78, 94, 86, 83, 80, 89],
    "Defense_Score": [89, 82, 89, 85, 86, 78, 85, 83, 80, 82, 88, 82, 84, 85, 86],
    "Home_Advantage": [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    "Match_Outcome": ["Win", "Win", "Draw", "Draw", "Lose", "Lose", "Win", "Win", "Draw", "Lose", "Win", "Draw", "Draw", "Lose", "Win"]
}

# 2. Convert the dictionary into a structured Pandas DataFrame
df = pd.DataFrame(match_data)

# 3. Export the DataFrame to a CSV file without including the index numbers
csv_filename = "football_matches.csv"
df.to_csv(csv_filename, index=False)

print(f"Success! '{csv_filename}' has been created with 15 rows of historical data.")