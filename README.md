# Twitter Trend Analyzer

## Purpose
The Twitter Trend Analyzer is a pipeline designed to scrape Twitter data and identify trends. It uses the Aineko framework to create a streaming workflow that processes real-time Twitter data.

## Design
The pipeline consists of two main nodes:

1. `TwitterScraperNode`: This node uses the Tweepy library to connect to the Twitter API and scrape tweets based on a specified query. It outputs the scraped tweet data to the `scraped_tweets` dataset.

2. `TrendIdentifierNode`: This node consumes the `scraped_tweets` dataset and applies logic to identify trends from the tweet data. The current implementation logs the tweet data, but this can be extended to include more sophisticated trend identification algorithms.

## Pipeline Configuration
The `pipeline.yml` file contains the configuration for the pipeline, including the nodes, datasets, and node parameters. The `TwitterScraperNode` is configured to search for tweets with the hashtag '#trending', in English, and of mixed result types. It retrieves up to 100 tweets per execution.

The `scraped_tweets` dataset is a Kafka stream that serves as the communication channel between the nodes.

## Running the Pipeline
To run the pipeline, ensure that the required environment variables for Twitter API credentials are set, and execute the pipeline using the Aineko CLI.

For more detailed instructions on running Aineko pipelines, refer to the Aineko documentation.
