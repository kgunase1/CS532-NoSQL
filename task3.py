import pymongo
import matplotlib.pyplot as plt

# Connect to MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['local']
collection = db['Spotify_Youtube']

# Define the aggregation pipeline
pipeline = [
   {
      "$match": { "Views": { "$gt": 1000000 } }
   },
   {
      "$group":
      {
         "_id": { "licensed": "$Licensed", "official_video": "$official_video" },
         "total_views": { "$sum": "$Views" },
         "total_likes": { "$sum": "$Likes" },
         "total_comments": { "$sum": "$Comments" },
         "count": { "$sum": 1 }
      }
   },
   {
      "$project":
      {
         "licensed": "$_id.licensed",
         "official_video": "$_id.official_video",
         "total_views": 1,
         "total_likes": 1,
         "total_comments": 1,
         "count": 1,
         "avg_views": { "$divide": ["$total_views", "$count"] },
         "avg_likes": { "$divide": ["$total_likes", "$count"] },
         "avg_comments": { "$divide": ["$total_comments", "$count"] }
      }
   },
   {
      "$sort":
      {
         "avg_views": -1
      }
   }
]

# Execute the aggregation pipeline and extract the results
results = list(collection.aggregate(pipeline))

# Create lists for each field
labels = ["{} - {}".format(result["_id"]["licensed"], result["_id"]["official_video"]) for result in results]
views = [result["avg_views"] for result in results]
likes = [result["avg_likes"] for result in results]
comments = [result["avg_comments"] for result in results]

# Create a multi-line chart using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(labels, views, label="Average Views")
ax.plot(labels, likes, label="Average Likes")
ax.plot(labels, comments, label="Average Comments")
ax.set_title("Relationship between Video Attributes and Popularity")
ax.set_xlabel("Licensed - Official Video")
ax.set_ylabel("Average Value")
ax.legend()
plt.xticks(rotation=45)
plt.show()
