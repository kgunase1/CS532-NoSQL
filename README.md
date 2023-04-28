# CS532-NoSQL

Task 1:
Recommending similar tracks to a given track - by using aggregation and the $lookup operator to join the Spotify and YouTube datasets based on artist and track name, it's possible to recommend similar tracks to a given track based on similar audio features and popularity.

$lookup - This stage joins the Spotify_Youtube collection with itself based on the Artist field. The result of this stage is a new array field called similarTracks that contains the data of all tracks by the same artist as the current track.

$unwind - This stage deconstructs the similarTracks array field created by the $lookup stage so that each document in the output represents a single track.

$match - This stage filters the documents to include only the tracks that match the given_track name, but exclude the track itself. This is done by using the $and operator to specify two conditions: the Track field must be equal to given_track, and the Track field of similarTracks must not be equal to given_track.

$project - This stage reshapes the documents in the pipeline to include only the fields that we want to output. The _id field is excluded, and a new Track field is created that contains the Track field of the similarTracks document. Additionally, a new field called SimilarityScore is created that uses the Euclidean distance formula to calculate the similarity between the current track and each similar track.

$sort - This stage sorts the documents in ascending order based on the SimilarityScore field.

Each stage in the pipeline modifies the documents in the input stream and passes the output to the next stage. The end result is a sorted list of similar tracks and their similarity scores, which

Task 2:
Analysis that finds tracks with similar audio features based on multiple criteria and sorts them by their popularity on YouTube and Spotify

In this example, we're filtering for tracks with a danceability score greater than or equal to 0.7, an energy score greater than or equal to 0.8, a tempo greater than or equal to 130, and a minimum of 1 million views on YouTube. We're also calculating the ratio of likes to views and sorting the results in descending order by this ratio. Finally, we're limiting the results to the top 10 most popular tracks that meet the specified criteria.

The output includes information about each track, including the track name, artist, danceability score, energy score, tempo, number of views, number of likes, like/view ratio, and title of the corresponding YouTube video. You can adjust the filtering and sorting criteria to match your specific needs.

Task 3:
Analyze the relationship between video attributes and video popularity: You can analyze the relationship between video attributes (such as licensed, official video, and live stream) and video popularity (based on views, likes, and comments on YouTube) to identify which attributes are most important for a music video's success and popularity.

Task 4:
Analyze the correlation between the audio features (such as danceability, energy, and valence) and the number of views and likes on YouTube. This analysis could reveal which features are most strongly associated with a song's popularity on YouTube.