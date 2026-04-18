import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs directory if it doesn't exist
os.makedirs('outputs', exist_ok=True)

print("Loading dataset...")
# Load dataset
df = pd.read_csv('data/customer_feedback.csv')

print(f"Dataset loaded successfully with {len(df)} rows.")

# 1. Clean Data (Handle missing values if any)
df.dropna(inplace=True)

print("Generating Visualizations...")

# 2. Satisfaction Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['SatisfactionScore'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Satisfaction Scores', fontsize=14)
plt.xlabel('Satisfaction Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('outputs/satisfaction_dist.png')
print("Saved satisfaction_dist.png")

# 3. Average Score by Country
country_scores = df.groupby('Country')['SatisfactionScore'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=country_scores.index, y=country_scores.values, palette='viridis')
plt.title('Average Satisfaction by Country', fontsize=14)
plt.xlabel('Country')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/country_scores.png')
print("Saved country_scores.png")

# 4. Loyalty Level Breakdown
loyalty_counts = df['LoyaltyLevel'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(loyalty_counts, labels=loyalty_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set2"))
plt.title('Loyalty Level Breakdown', fontsize=14)
plt.savefig('outputs/loyalty_breakdown.png')
print("Saved loyalty_breakdown.png")

print("EDA Analysis completed. Check the 'outputs' folder for the charts.")
