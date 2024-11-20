import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_name = 'spotify_songs_dataset.csv'  # Replace with your file path if it's in a different location
try:
    data = pd.read_csv(file_name)
    print("Data Loaded Successfully!")
except FileNotFoundError:
    print("File not found. Please ensure the file exists in the specified location.")
    exit()

# Display the first few rows of the data
print("\nSample Data:")
print(data.head())

# Data Cleaning: Handle missing values
data['duration'] = data['duration'].fillna(data['duration'].mean())  # Fill missing durations with the mean
data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')  # Convert release_date to datetime

# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Visualization
# 1. Popularity by Genre
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='genre', y='popularity', ci=None, palette='viridis')
plt.title('Popularity by Genre')
plt.xlabel('Genre')
plt.ylabel('Popularity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Number of Songs by Release Year
data['release_year'] = data['release_date'].dt.year
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='release_year', order=sorted(data['release_year'].dropna().unique()), palette='cubehelix')
plt.title('Number of Songs by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Duration Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['duration'], kde=True, bins=20, color='blue')
plt.title('Song Duration Distribution')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Top Labels by Song Count
top_labels = data['label'].value_counts().head(5)
plt.figure(figsize=(10, 6))
top_labels.plot(kind='bar', color='orange')
plt.title('Top 5 Labels by Song Count')
plt.xlabel('Label')
plt.ylabel('Number of Songs')
plt.tight_layout()
plt.show()
