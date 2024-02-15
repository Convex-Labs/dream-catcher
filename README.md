# Synthetic Log Streamer

The Synthetic Log Streamer is a pipeline designed to process a synthetic log stream and interact with OpenAI for analysis. The pipeline generates synthetic log data at regular intervals, each with a timestamp, log level, and message. These logs are then passed to an OpenAI interactor node, which uses OpenAI's language model to analyze the log entries.

## Nodes

### SyntheticLogGenerator
This node generates synthetic log data with varying log levels (INFO, WARNING, ERROR) and timestamps. It simulates a real-world log stream. The log levels are chosen using a secure random choice to address security concerns.

### OpenAIInteractor
This node takes the synthetic log entries and sends them to OpenAI's language model for analysis. The analysis results are then produced to the `log_analysis` dataset.

## Pipeline

The pipeline is configured with two nodes: `LogGenerator` and `OpenAIInteractor`. The `LogGenerator` node produces synthetic log data to the `synthetic_log` dataset, which is then consumed by the `OpenAIInteractor` node. The analysis results are produced to the `log_analysis` dataset.

The pipeline utilizes Kafka streams to manage the datasets, allowing for real-time processing and analysis of the synthetic log data.