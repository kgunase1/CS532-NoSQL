import pymongo
import numpy as np
import matplotlib.pyplot as plt


client = pymongo.MongoClient()
db = client['local']
collection = db['Spotify_Youtube']

popularity_threshold = 1000000

pipeline = [
    {"$match": {"Views": {"$gte": popularity_threshold}}},
    {"$group": {"_id": "$Album_type",
                "danceability_avg": {"$avg": "$Danceability"},
                "energy_avg": {"$avg": "$Energy"},
                "tempo_avg": {"$avg": "$Tempo"},
                "views_avg": {"$avg": "$Views"},
                "likes_avg": {"$avg": "$Likes"}}},
    {"$project": {"_id": 0, "genre": "$_id", "danceability": "$danceability_avg",
                  "energy": "$energy_avg", "tempo": "$tempo_avg",
                  "views": "$views_avg", "likes": "$likes_avg"}},
    {"$sort": {"views": -1}}
]

result = list(collection.aggregate(pipeline))

# Create a scatter plot of danceability vs. energy, color-coded by views and size-coded by likes
genres = [r['genre'] for r in result]
danceability = [r['danceability'] for r in result]
energy = [r['energy'] for r in result]
views = [r['views'] for r in result]
likes = [r['likes'] for r in result]

fig, ax = plt.subplots()
scatter = ax.scatter(danceability, energy, c=views, cmap='cool', alpha=0.8, s=np.array(likes)/10000)
ax.set_xlabel('Danceability')
ax.set_ylabel('Energy')
cbar = plt.colorbar(scatter)
cbar.set_label('Average Views')
for i, genre in enumerate(genres):
    ax.annotate(genre, (danceability[i], energy[i]))
plt.show()
