# Log Urgency Classifier

The Log Urgency Classifier project is designed to ingest logs from a synthetic log producer, classify the logs using a machine learning model into urgency categories, and take appropriate actions based on the level of urgency.

## Nodes

### LogProducer
The `LogProducer` node simulates the production of log entries. It generates random log entries and sends them to the `raw_logs` dataset.

### LogClassifier
The `LogClassifier` node consumes raw logs and classifies them into urgency categories ('low', 'medium', 'high'). The classification is currently simulated using random choices from the `secrets` module for enhanced security. The classified logs are then sent to the `classified_logs` dataset.

### UrgencyAction
The `UrgencyAction` node consumes classified logs and takes actions based on the urgency level. Actions for 'high', 'medium', and 'low' urgency logs are to be defined according to the operational requirements.

## Pipeline
The pipeline is configured in `pipeline.yml` and consists of the three nodes described above, connected through `raw_logs` and `classified_logs` datasets. The `raw_logs` dataset is produced by `LogProducer` and consumed by `LogClassifier`. The `classified_logs` dataset is produced by `LogClassifier` and consumed by `UrgencyAction`.

The project is built using the Aineko framework, ensuring real-time processing and flexibility to integrate actual machine learning models for log classification and define specific actions for each urgency level.