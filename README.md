# Movie Tracker

The Movie Tracker project is designed to keep track of new movie releases and provide recommendations based on user preferences. It utilizes the Aineko framework to process streaming data and apply real-time analytics.

## Nodes

### MovieFetcherNode

The `MovieFetcherNode` connects to an external movie database API to fetch the latest movies that are currently playing in theaters. It filters the movies based on the availability and sends the list to the `new_movies` dataset. The node includes error handling for timeouts and other request exceptions to ensure reliability.

### RecommendationEngineNode

The `RecommendationEngineNode` consumes the `new_movies` dataset and applies user preferences to recommend movies. It matches the movies against the preferences such as genre and minimum rating and produces a list of recommended movies to the `recommended_movies` dataset.

## Pipeline

The pipeline is configured with two main nodes: `MovieFetcher` and `RecommendationEngine`. The `MovieFetcher` node is responsible for fetching new movie data, and the `RecommendationEngine` node processes this data to generate recommendations. The pipeline uses Kafka streams as datasets to facilitate real-time data processing and communication between nodes.