# Log Consolidator

The Log Consolidator is a project designed to streamline the process of collecting, categorizing, and alerting on logs from various sources. It uses a machine learning model to categorize logs by urgency and sends alerts for the most urgent logs through Slack.

## Nodes

### LogCollector
This node is responsible for collecting logs from different sources. It can be extended to fetch logs from APIs, file systems, or any other log-producing services. The node includes a timeout in the requests call to prevent hanging.

### LogCategorizer
The LogCategorizer node consumes the raw logs and uses a machine learning model to categorize them by urgency. It produces categorized logs for further processing.

### SlackNotifier
The SlackNotifier node consumes the categorized logs and filters out the ones with high urgency. It sends alerts for these logs to a configured Slack channel using a webhook with a timeout to ensure the request does not hang.

## Pipeline

The pipeline is configured to run the above nodes in sequence, processing streaming data in real-time. The `raw_logs` dataset acts as the input for the LogCategorizer, which then outputs to the `categorized_logs` dataset. The SlackNotifier consumes from `categorized_logs` to send alerts.

The pipeline is designed to be robust and scalable, allowing for easy addition of new log sources and urgency categorization methods.

## Getting Started

To get started with the Log Consolidator, set up the necessary environment variables for your log sources and Slack webhook URL. Then, deploy the pipeline and monitor your Slack channel for alerts on urgent logs.

## Design Considerations

The design of the nodes and pipeline ensures that the system is modular and each component can be independently updated or replaced. The use of streaming datasets allows for real-time processing and alerting, which is crucial for log management systems.

The machine learning model for categorizing logs can be trained on historical data to improve accuracy over time. The SlackNotifier can be configured to send alerts to different channels based on the type of log or level of urgency.
