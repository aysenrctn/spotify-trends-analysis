import pandas as pd

# Read the CSV file
df=pd.read_csv("Spotify most streamed.csv")
print(df.head(10))

#Print number of missing data
print("\nThe number of missing values:")
print(df.isnull().sum())

# Remove commas in 'Daily', convert errors to NaN, fill NaN with 0, and convert to int
df['Daily'] = pd.to_numeric(df['Daily'].str.replace(",", ""), errors='coerce').fillna(0).astype(int)

# Do the same for 'Streams'
df['Streams'] = pd.to_numeric(df['Streams'].str.replace(",", ""), errors='coerce').fillna(0).astype(int)

# Split 'Artist and Title' column into artist and title
split_cols = df['Artist and Title'].str.split(" - ", n=1, expand=True)

# If only artist exists, set title as 'Unknown'
df['Artist'] = split_cols[0]
df['Title'] = split_cols[1].fillna("Unknown")

# Drop the original 'Artist and Title' column
df = df.drop(columns=['Artist and Title'])

# Sort songs by total streams descending
sorted_by_streams = df.sort_values('Streams', ascending=False)

# Sort songs by daily streams descending
sorted_by_daily = df.sort_values('Daily', ascending=False)

#Remove unnecessary columns if it exists
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Print top 5 songs by total streams
print("\nTop 5 songs by total streams:")
print(sorted_by_streams[['Artist', 'Title', 'Streams']].head(5))

# Print top 5 songs by daily streams
print("\nTop 5 songs by daily streams:")
print(sorted_by_daily[['Artist', 'Title', 'Daily']].head(5))

# Calculate average streaming by artist
print(df.groupby("Artist")[["Streams", "Daily"]].mean())

# Print column names for checking
print(df.columns)
# Result: There is no 'Popularity' column yet

#Import numpy for random number generation
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Add new columns: 'Likes' and 'Followers' with random values
df['Likes'] = np.random.randint(1_000, 100_000, size=len(df))
df['Followers'] = np.random.randint(10_000, 1_000_000, size=len(df))

# Update 'Streams' and 'Daily' with new random values
df['Streams'] = np.random.randint(1_000_000, 2_000_000_000, size=len(df))
df['Daily'] = np.random.randint(10_000, 2_000_000, size=len(df))

# Normalize the data using MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

# Normalize selected columns and store in new columns
df[['Streams_norm', 'Daily_norm', 'Likes_norm', 'Followers_norm']] = scaler.fit_transform(
    df[['Streams', 'Daily', 'Likes', 'Followers']]
)

# We are calculating the popularity score.
# We use Streams, Daily, Likes, and Followers columns for this.
# Each one has a different weight: Streams 40%, the others 20%.
# This helps us find out which songs are the most popular.
df['Popularity'] = (
    df['Streams_norm'] * 0.4 +
    df['Daily_norm'] * 0.2 +
    df['Likes_norm'] * 0.2 +
    df['Followers_norm'] * 0.2
) * 100

# Print first 10 artists and their popularity scores
print(df[['Artist', 'Popularity']].head(10))

# Print popularity statistics
print(df['Popularity'].describe())

# Save the enriched data to a new CSV file
df.to_csv("spotify_enriched.csv", index=False)