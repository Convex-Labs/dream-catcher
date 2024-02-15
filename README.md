# Sentiment Analyzer

The Sentiment Analyzer project is designed to analyze the sentiment of text data in real-time and categorize it as positive, negative, or neutral. This project uses the Aineko framework to process streaming text data through a sentiment analysis pipeline.

## Design

The core of the project is the `SentimentAnalysisNode`, which is responsible for performing sentiment analysis on each piece of text it receives. It uses the VADER sentiment analysis tool to calculate the sentiment score and categorizes the text accordingly.

The pipeline is configured to read text data from an input dataset, process it through the sentiment analysis node, and output the results to a result dataset. Both datasets are implemented as Kafka streams, allowing for scalable and real-time data processing.

## Usage

To use the Sentiment Analyzer, text data should be produced to the `input_text` dataset. The pipeline will then process the data and output the sentiment analysis results to the `sentiment_result` dataset. Clients can consume these results in real-time to take further actions based on the sentiment of the text.
