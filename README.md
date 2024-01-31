# Movie Tracker

## Overview

The Movie Tracker project is designed to keep track of new movie releases and provide personalized recommendations based on user preferences. It utilizes a pipeline that fetches new movie data and processes it to match with user-defined criteria.

## Nodes

### MovieFetcherNode

This node is responsible for fetching the latest movies that are currently playing in theaters. It connects to an external movie database API and retrieves the list of new releases. It includes a timeout in the requests call to handle potential delays in the response.

### RecommendationEngineNode

The Recommendation Engine Node takes the new movie data and user preferences as input. It processes this information to generate a list of recommended movies that align with the user's preferred genres.

## Pipeline

The pipeline is configured with two main nodes: `MovieFetcher` and `RecommendationEngine`. The `MovieFetcher` node produces a stream of new movies, which is then consumed by the `RecommendationEngine` node along with user preferences to produce personalized movie recommendations.