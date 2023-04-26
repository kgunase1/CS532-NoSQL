from pymongo import MongoClient
import math
import matplotlib.pyplot as plt

client = MongoClient('mongodb://localhost:27017/')
db = client['local']
collection = db['Spotify_Youtube']

# Specify the given track for which we want to find similar tracks
given_track = "Feel Good Inc."

# Use the $lookup operator to join the Spotify and YouTube data based on artist and track name
pipeline = [
    {
        '$lookup': {
            'from': 'Spotify_Youtube',
            'localField': 'Artist',
            'foreignField': 'Artist',
            'as': 'similarTracks'
        }
    },
    {
        '$unwind': '$similarTracks'
    },
    {
        '$match': {
            '$and': [
                {'Track': given_track},
                {'similarTracks.Track': {'$ne': given_track}}
            ]
        }
    },
    {
        '$project': {
            '_id': 0,
            'Track': '$similarTracks.Track',
            'SimilarityScore': {
                '$sqrt': {
                    '$add': [
                        {'$pow': [{'$subtract': ['$Danceability', '$similarTracks.Danceability']}, 2]},
                        {'$pow': [{'$subtract': ['$Energy', '$similarTracks.Energy']}, 2]},
                        {'$pow': [{'$subtract': ['$Key', '$similarTracks.Key']}, 2]},
                        {'$pow': [{'$subtract': ['$Loudness', '$similarTracks.Loudness']}, 2]},
                        {'$pow': [{'$subtract': ['$Speechiness', '$similarTracks.Speechiness']}, 2]},
                        {'$pow': [{'$subtract': ['$Acousticness', '$similarTracks.Acousticness']}, 2]},
                        {'$pow': [{'$subtract': ['$Instrumentalness', '$similarTracks.Instrumentalness']}, 2]},
                        {'$pow': [{'$subtract': ['$Liveness', '$similarTracks.Liveness']}, 2]},
                        {'$pow': [{'$subtract': ['$Valence', '$similarTracks.Valence']}, 2]},
                        {'$pow': [{'$subtract': ['$Tempo', '$similarTracks.Tempo']}, 2]}
                    ]
                }
            }
        }
    },
    {
        '$sort': {'SimilarityScore': 1}
    }
]

result = list(collection.aggregate(pipeline))

# Extract the track names and similarity scores from the result
tracks = [r["Track"] for r in result]
scores = [math.ceil(r["SimilarityScore"]) for r in result]

# Plot the bar chart
plt.bar(tracks, scores)
plt.xticks(rotation=45)
plt.xlabel("Track")
plt.ylabel("Similarity Score (rounded up)")
plt.title("Top Similar Tracks to %s" % given_track)
plt.show()
