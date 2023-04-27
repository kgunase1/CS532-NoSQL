# CS532-NoSQL

Task 1:
Recommending similar tracks to a given track - by using aggregation and the $lookup operator to join the Spotify and YouTube datasets based on artist and track name, it's possible to recommend similar tracks to a given track based on similar audio features and popularity.

Task 2:
Analysis that finds tracks with similar audio features based on multiple criteria and sorts them by their popularity on YouTube and Spotify

In this example, we're filtering for tracks with a danceability score greater than or equal to 0.7, an energy score greater than or equal to 0.8, a tempo greater than or equal to 130, and a minimum of 1 million views on YouTube. We're also calculating the ratio of likes to views and sorting the results in descending order by this ratio. Finally, we're limiting the results to the top 10 most popular tracks that meet the specified criteria.

The output includes information about each track, including the track name, artist, danceability score, energy score, tempo, number of views, number of likes, like/view ratio, and title of the corresponding YouTube video. You can adjust the filtering and sorting criteria to match your specific needs.

Task 3:
Analyze the relationship between video attributes and video popularity: You can analyze the relationship between video attributes (such as licensed, official video, and live stream) and video popularity (based on views, likes, and comments on YouTube) to identify which attributes are most important for a music video's success and popularity.