import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. Load and Explore
# ---------------------------------------------------------
# Load data/clean_data.csv into a Pandas DataFrame
df = pd.read_csv('data/clean_data.csv')

# Print the first 5 rows
print("First 5 rows:")
print(df.head())

# Print the shape of the DataFrame (rows and columns)
print(f"Loaded data: {df.shape}")

# Print the average score and average num_comments across all stories
avg_score = df['score'].mean()
avg_comments = df['num_comments'].mean()
print(f"Average score   : {avg_score:,.0f}")
print(f"Average comments: {avg_comments:,.0f}")

print("\n--- NumPy Stats ---")

# ---------------------------------------------------------
# 2. Basic Analysis with NumPy
# ---------------------------------------------------------
# Use NumPy to access columns as arrays and compute stats
scores_array = df['score'].to_numpy()

# What is the mean, median, and standard deviation of score?
mean_score = np.mean(scores_array)
median_score = np.median(scores_array)
std_score = np.std(scores_array)

print(f"Mean score      : {mean_score:,.0f}")
print(f"Median score    : {median_score:,.0f}")
print(f"Std deviation   : {std_score:,.0f}")

# What is the highest score and lowest score?
max_score = np.max(scores_array)
min_score = np.min(scores_array)

print(f"Max score       : {max_score:,.0f}")
print(f"Min score       : {min_score:,.0f}\n")

# Which category has the most stories?
top_category = df['category'].mode()[0]
top_category_count = (df['category'] == top_category).sum()
print(f"Most stories in: {top_category} ({top_category_count} stories)")

# Which story has the most comments? Print its title and comment count
most_commented_idx = df['num_comments'].idxmax()
most_commented_story = df.loc[most_commented_idx]
print(f'Most commented story: "{most_commented_story["title"]}" - {most_commented_story["num_comments"]:,} comments\n')

# ---------------------------------------------------------
# 3. Add New Columns
# ---------------------------------------------------------
# Formula for engagement: num_comments / (score + 1)
df['engagement'] = df['num_comments'] / (df['score'] + 1)

# Formula for is_popular: True if score > average score, else False
df['is_popular'] = df['score'] > avg_score

# ---------------------------------------------------------
# 4. Save the Result
# ---------------------------------------------------------
# Save the updated DataFrame to data/trends_analysed.csv
df.to_csv('data/trends_analysed.csv', index=False)
print("saved to data/trends_analysed.csv")