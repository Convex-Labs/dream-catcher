# LogAlert

LogAlert is a real-time log consolidation and alerting application. It ingests logs from various sources, categorizes them based on urgency levels using a machine learning model, and sends alerts to a configured Slack channel for critical logs.

## Design

The application is designed around two main components:

- `LogCategorizer`: This node processes incoming log entries and categorizes them into urgency levels. The current implementation uses a simple keyword-based approach for demonstration purposes.

- `SlackNotifier`: This node listens for categorized log entries marked as critical and sends an alert message to a Slack channel using a webhook URL. The node has been updated to include a timeout in the request to address a potential security concern identified by Bandit.

## Pipeline

The pipeline is configured to stream logs through Kafka topics, where `LogCategorizer` consumes from the `log_input` topic, processes the logs, and produces categorized logs to the `categorized_log` topic. The `SlackNotifier` node then consumes from the `categorized_log` topic and sends alerts for critical logs.

To deploy and run the LogAlert application, ensure that the Kafka streams are properly set up and that the Slack webhook URL is correctly configured in the `pipeline.yml` file.