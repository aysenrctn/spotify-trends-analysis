# Import cleaned data and sorted dataframe
from data_cleaning import df, sorted_by_streams

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Select top 10 most streamed songs
top10= sorted_by_streams.head(10)

# Bar chart for top 10 most streamed songs
plt.figure(figsize=(10,6))
plt.barh(top10['Title'], top10['Streams'], color='salmon')
plt.xlabel('Total Streams')
plt.title('Top 10 Most Streamed Songs')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Group total streams by artist
artist_streams = df.groupby('Artist')['Streams'].sum().sort_values(ascending=False).head(10)

# Pie chart for top 10 artists by total streams
plt.figure(figsize=(8,8))
plt.pie(
    artist_streams,
    labels=artist_streams.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Paired.colors
)


plt.title('Top 10 Artists by Total Streams (Pie Chart)')
plt.tight_layout()
plt.show()

# Calculate popularity per stream
df['Popularity_per_Stream'] = df['Popularity'] / df['Streams']

# Get top 10 songs by popularity efficiency
top_eff = df.sort_values('Popularity_per_Stream', ascending=False).head(10)

# Bar chart for top 10 songs by popularity per stream
plt.figure(figsize=(10,6))
plt.barh(top_eff['Title'], top_eff['Popularity_per_Stream'], color='mediumseagreen')
plt.xlabel('Popularity per Stream')
plt.title('Top 10 Songs by Popularity Efficiency')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# Import seaborn for heatmap
import seaborn as sns

# Create correlation matrix between numerical columns
corr = df.corr(numeric_only=True)

# Draw heatmap of correlations
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.show()



# Calculate average popularity score per artist
artist_popularity = df.groupby('Artist')['Popularity'].mean().sort_values(ascending=False).head(10)
artist_popularity.plot(kind='bar', color='mediumslateblue')
plt.title('Top 10 Artists by Custom Popularity Score')

# Plot bar chart for top 10 artists by average popularity
plt.figure(figsize=(10,6))

# Annotate each bar with its value
bars = artist_popularity.plot(kind='bar', color='mediumslateblue')
for bar in bars.patches:
    bars.annotate(format(bar.get_height(), '.1f'),
                  (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                  ha='center', va='bottom')

plt.ylabel('Average Popularity Score')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.show()
