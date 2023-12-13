# Twitter Trend Analyzer

## Purpose
The Twitter Trend Analyzer is a pipeline designed to scrape Twitter data and identify trending topics. It leverages the Aineko framework to create a streaming workflow that processes real-time Twitter data.

## Design
The pipeline consists of two main nodes:

1. `TwitterScraperNode`: This node uses the Tweepy library to interact with the Twitter API. It fetches tweets based on a specified query and count, and then produces a list of tweets to the `scraped_tweets` dataset.

2. `TrendIdentifierNode`: This node consumes the `scraped_tweets` dataset, extracts hashtags from the tweets, and identifies the most common hashtags to determine trends. The top trends are then produced to the `identified_trends` dataset.

## Pipeline Configuration
The `pipeline.yml` file configures the pipeline with the two nodes and their respective inputs and outputs. It also defines the datasets used for communication between nodes.

The `TwitterScraperNode` is configured to search for tweets with the hashtag '#trending' by default, but this can be customized through the `node_params`. The `TrendIdentifierNode` takes the output from the `TwitterScraperNode` and processes it to identify trends.

## Usage
To use this pipeline, you will need to set up the necessary Twitter API credentials as environment variables. The pipeline can then be executed using the Aineko framework, and it will continuously process Twitter data to identify and update trending topics in real-time.
