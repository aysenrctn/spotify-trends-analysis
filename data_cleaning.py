import pandas as pd

df=pd.read_csv("Spotify most streamed.csv")
print(df.head(10))

#number of missing data
print("\nThe number of missing values:")
print(df.isnull().sum())

# Removes the , character from numbers. Converts incorrect or missing data to NaN. Fills missing data with 0. Converts the results to integers.
df['Daily'] = pd.to_numeric(df['Daily'].str.replace(",", ""), errors='coerce').fillna(0).astype(int)

df['Streams'] = pd.to_numeric(df['Streams'].str.replace(",", ""), errors='coerce').fillna(0).astype(int)

# separate artist and title
split_cols = df['Artist and Title'].str.split(" - ", n=1, expand=True)

# Eksik olanlara özel işlem: sadece sanatçı varsa, şarkı adı 'Unknown' olsun
df['Artist'] = split_cols[0]
df['Title'] = split_cols[1].fillna("Unknown")

# Orijinal sütunu kaldır
df = df.drop(columns=['Artist and Title'])

# sort descending for the total listening
sorted_by_streams = df.sort_values('Streams', ascending=False)

#most popular song by the daily listening
sorted_by_daily = df.sort_values('Daily', ascending=False)

#Remove any unnecessary columns
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

print("\nTop 5 songs by total streams:")
print(sorted_by_streams[['Artist', 'Title', 'Streams']].head(5))

print("\nTop 5 songs by daily streams:")
print(sorted_by_daily[['Artist', 'Title', 'Daily']].head(5))

#Average Streaming by Artist
print(df.groupby("Artist")[["Streams", "Daily"]].mean())

print(df.columns)
#there is not popularity column

import numpy as np

np.random.seed(42)
df['Likes'] = np.random.randint(1_000, 100_000, size=len(df))
df['Followers'] = np.random.randint(10_000, 1_000_000, size=len(df))
df['Streams'] = np.random.randint(1_000_000, 2_000_000_000, size=len(df))
df['Daily'] = np.random.randint(10_000, 2_000_000, size=len(df))

#normalization
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[['Streams_norm', 'Daily_norm', 'Likes_norm', 'Followers_norm']] = scaler.fit_transform(
    df[['Streams', 'Daily', 'Likes', 'Followers']]
)

#popularity process
df['Popularity'] = (
    df['Streams_norm'] * 0.4 +
    df['Daily_norm'] * 0.2 +
    df['Likes_norm'] * 0.2 +
    df['Followers_norm'] * 0.2
) * 100

print(df[['Artist', 'Popularity']].head(10))
print(df['Popularity'].describe())



print(df.columns)


df.to_csv("spotify_enriched.csv", index=False)