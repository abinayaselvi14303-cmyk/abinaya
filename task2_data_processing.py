import pandas as pd
import glob
import os

# 1. Load the JSON File
# Locate the json file in data/ folder (e.g., data/trends_20240115.json)
json_files = glob.glob('data/trends_*.json')
file_path = json_files[0] if json_files else 'data/trends_20240115.json'

df = pd.read_json(file_path)
print(f"Loaded {len(df)} stories from {file_path}")

# 2. Clean the Data

# Duplicates - remove any rows with the same post_id
df = df.drop_duplicates(subset=['post_id'])
print(f"After removing duplicates: {len(df)}")

# Missing values - drop rows where post_id, title, or score is missing
df = df.dropna(subset=['post_id', 'title', 'score'])
print(f"After removing nulls: {len(df)}")

# Data types - make sure score and num_comments are integers
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)

# Low quality - remove stories where score is less than 5
df = df[df['score'] >= 5]
print(f"After removing low scores: {len(df)}")

# Whitespace - strip extra spaces from the title column
df['title'] = df['title'].astype('str').str.strip()

# 3. Save as CSV
# Ensure output directory exists
os.makedirs('data', exist_ok=True)
output_path = 'data/trends_clean.csv'

# Save cleaned dataframe to CSV without index
df.to_csv(output_path, index=False)
print(f"\nSaved {len(df)} rows to {output_path}")

# Print summary: stories per category
print("\nStories per category:")
print(df['category'].value_counts().to_string(header=False))