# Movie Tracker

## Overview

The Movie Tracker project is designed to keep track of new movie releases and provide personalized recommendations based on user preferences. It utilizes a pipeline that fetches new movie data and filters them according to the user's likes and interests.

## Nodes

### MovieFetcherNode

This node is responsible for fetching the latest movies that are currently playing in theaters. It uses The Movie Database (TMDb) API to retrieve the data. The node includes a timeout setting for the API request to ensure that the system remains responsive even if the external service is slow or unresponsive.

### RecommendationEngineNode

After fetching the new releases, this node takes user preferences and the list of new movies to generate recommendations. It filters the movies based on the criteria provided in the user preferences.

## Pipeline

The pipeline is composed of two main nodes: `MovieFetcher` and `RecommendationEngine`. The `MovieFetcher` node outputs the list of new movies to the `new_movies` dataset, which is then consumed by the `RecommendationEngine` node. The `RecommendationEngine` node also consumes user preferences from the `user_preferences` dataset and produces the final recommendations to the `movie_recommendations` dataset.