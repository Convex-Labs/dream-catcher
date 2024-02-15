# Sentiment Analyzer

The Sentiment Analyzer project is designed to analyze the sentiment of text using the output from a language model (LLM). The project uses the Aineko framework to process the text in real-time and determine if the sentiment is positive, negative, or neutral based on the compound score calculated by the VADER Sentiment Analysis tool.

## Nodes

- `SentimentAnalyzerNode`: This node consumes the output text from an LLM and uses the VADER Sentiment Analysis tool to calculate the sentiment score. It then categorizes the sentiment as positive, negative, or neutral and produces the result to the `sentiment_analysis` dataset.

## Pipeline

The pipeline is configured to use the `SentimentAnalyzerNode` to process the text. It consumes data from the `llm_output` dataset and produces the sentiment analysis result to the `sentiment_analysis` dataset.

The pipeline is defined in the `pipeline.yml` file, which specifies the input and output datasets, as well as the node class to be used for processing.

To run the pipeline, ensure that the Aineko framework is properly set up and execute the pipeline configuration using the appropriate Aineko CLI commands.
