# Twitter Trend Analyzer

This project contains a pipeline that scrapes Twitter data to identify trends. It is designed to be simple and easy to understand while fully expressing the required functionality.

## Pipeline Design

The pipeline consists of two main nodes:

1. `TwitterScraperNode`: This node uses the Tweepy library to authenticate with the Twitter API and fetch the latest trending topics worldwide.

2. `TrendIdentifierNode`: This node consumes the data produced by the TwitterScraperNode, processes it to identify the most significant trends based on tweet volume, and produces a list of identified trends.

## How to Run

To run this pipeline, you will need to set the following environment variables with your Twitter API credentials:

- `TWITTER_API_KEY`
- `TWITTER_API_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_SECRET`

Once the environment variables are set, you can start the pipeline using the Aineko framework.

## Nodes and Pipeline Configuration

The `nodes.py` file contains the implementation of the nodes using the Aineko framework. The `pipeline.yml` file contains the pipeline configuration, defining how the nodes are connected and the datasets they use.

The nodes are designed to be modular and can be easily extended or replaced to accommodate different sources of data or methods of trend identification.