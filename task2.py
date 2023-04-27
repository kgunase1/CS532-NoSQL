from pymongo import MongoClient
import math
import matplotlib.pyplot as plt
import sys

client = MongoClient('mongodb://localhost:27017/')
db = client['local']
collection = db['Spotify_Youtube']


# Define the audio features to match on
danceability_min = 0.7
energy_min = 0.8
tempo_min = 130

# Define the minimum number of views for a track to be considered popular
popularity_threshold = 1000000

pipeline = [
    {"$match": {"Danceability": {"$gte": danceability_min},
                "Energy": {"$gte": energy_min},
                "Tempo": {"$gte": tempo_min},
                "Views": {"$gte": popularity_threshold}}},
    {"$project": {"Track": 1, "Artist": 1, "Danceability": 1, "Energy": 1, "Tempo": 1, "Views": 1, "Likes": 1, "Title": 1}},
    {"$addFields": {"like_ratio": {"$divide": ["$Likes", "$Views"]}}},
    {"$sort": {"like_ratio": -1}},
    {"$limit": 10}
]

result = collection.aggregate(pipeline)

# Create a dictionary to store the data for the graph
data = {}
for song in result:
    data[song['Track'] + " by " + song['Artist']] = song['like_ratio']

print(data)
# Plot the graph
plt.bar(data.keys(), data.values())
plt.xticks(rotation=90)
plt.xlabel("Tracks")
plt.ylabel("Like/View Ratio")
plt.title("Top 10 Popular Tracks on Spotify and YouTube")
plt.show()
