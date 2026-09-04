import os
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Setup
# ---------------------------------------------------------
# Load data/trends_analysed.csv into a DataFrame
df = pd.read_csv('data/trends_analysed.csv')

# Create a folder called outputs/ if it doesn't exist
os.makedirs('outputs', exist_ok=True)

# ---------------------------------------------------------
# 2. Chart 1: Top 10 Stories by Score
# ---------------------------------------------------------
# Create a horizontal bar chart showing top 10 stories by score
plt.figure(figsize=(10, 6))
top_10 = df.nlargest(10, 'score').sort_values('score', ascending=True)

# Truncate titles longer than 30 characters
short_titles = [t[:30] + '...' if len(t) > 30 else t for t in top_10['title']]

plt.barh(short_titles, top_10['score'], color='skyblue')
plt.title('Top 10 Stories by Score')
plt.xlabel('Score')
plt.ylabel('Story Title')

plt.savefig('outputs/charts_top_stories.png', bbox_inches='tight')
plt.savefig('outputs/charts_top_stories.jpg', bbox_inches='tight')  # Saved for safety
plt.close()

# ---------------------------------------------------------
# 3. Chart 2: Stories per Category
# ---------------------------------------------------------
# Create a bar chart showing how many stories came from each category
plt.figure(figsize=(8, 5))
category_counts = df['category'].value_counts()

# Use a different color for each bar
colors = plt.cm.Set3(range(len(category_counts)))

plt.bar(category_counts.index, category_counts.values, color=colors)
plt.title('Stories per Category')
plt.xlabel('Category')
plt.ylabel('Number of Stories')
plt.xticks(rotation=45)

plt.savefig('outputs/charts_categories.png', bbox_inches='tight')
plt.savefig('outputs/charts_categories.jpg', bbox_inches='tight')
plt.close()

# ---------------------------------------------------------
# 4. Chart 3: Score vs Comments
# ---------------------------------------------------------
# Create a scatter plot with score on X-axis and num_comments on Y-axis
plt.figure(figsize=(8, 6))

# Color points differently for popular vs non-popular stories
popular = df[df['is_popular'] == True]
non_popular = df[df['is_popular'] == False]

plt.scatter(non_popular['score'], non_popular['num_comments'], color='gray', label='Not Popular', alpha=0.6)
plt.scatter(popular['score'], popular['num_comments'], color='red', label='Popular', alpha=0.8)

plt.title('Score vs Comments')
plt.xlabel('Score')
plt.ylabel('Number of Comments')
plt.legend()

plt.savefig('outputs/charts_scatter.png', bbox_inches='tight')
plt.savefig('outputs/charts_scatter.jpg', bbox_inches='tight')
plt.close()

# ---------------------------------------------------------
# Bonus — Dashboard
# ---------------------------------------------------------
# Combine all 3 charts into a single figure using subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Subplot 1: Top 10 Stories
axes[0].barh(short_titles, top_10['score'], color='skyblue')
axes[0].set_title('Top 10 Stories by Score')
axes[0].set_xlabel('Score')

# Subplot 2: Categories
axes[1].bar(category_counts.index, category_counts.values, color=colors)
axes[1].set_title('Stories per Category')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Number of Stories')
axes[1].tick_params(axis='x', rotation=45)

# Subplot 3: Scatter Plot
axes[2].scatter(non_popular['score'], non_popular['num_comments'], color='gray', label='Not Popular', alpha=0.6)
axes[2].scatter(popular['score'], popular['num_comments'], color='red', label='Popular', alpha=0.8)
axes[2].set_title('Score vs Comments')
axes[2].set_xlabel('Score')
axes[2].set_ylabel('Number of Comments')
axes[2].legend()

# Add a overall title
fig.suptitle('TrendPulse Dashboard', fontsize=16)
plt.tight_layout()

# Save as dashboard.png
plt.savefig('outputs/dashboard.png', bbox_inches='tight')
plt.savefig('outputs/dashboard.jpg', bbox_inches='tight')
plt.close()

print("All charts and dashboard generated successfully in outputs/ directory!")