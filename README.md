# Twitter Trend Analyzer

## Overview

The Twitter Trend Analyzer is a project designed to scrape Twitter data and identify trending hashtags in real-time. This project uses the Aineko framework to create a pipeline that consists of two main nodes: `TwitterScraperNode` and `TrendIdentifierNode`.

## Nodes

### TwitterScraperNode

This node uses the Tweepy library to interact with the Twitter API. It searches for tweets based on a specified query, language, and result type. The scraped tweets are then produced to the `scraped_tweets` dataset.

### TrendIdentifierNode

The TrendIdentifierNode consumes tweets from the `scraped_tweets` dataset and processes the text to identify hashtags. It keeps a count of the occurrences of each hashtag and produces the current trend statistics to the `identified_trends` dataset.

## Pipeline

The pipeline configuration is defined in `pipeline.yml`. It connects the two nodes and their respective datasets to form a streaming workflow. The `TwitterScraperNode` is configured to output to `scraped_tweets`, which is then consumed by the `TrendIdentifierNode`. The latter outputs to `identified_trends`, which can be used to monitor the trending hashtags.

## Setup

To run this project, you will need to set up Twitter API credentials as environment variables. The node code will use these credentials to authenticate with the Twitter API.

## Usage

Once the pipeline is running, it will continuously scrape Twitter for the latest tweets based on the configured parameters and update the trend statistics in real-time.
