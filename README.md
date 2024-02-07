# Log Classifier Project

## Purpose
The Log Classifier project is designed to ingest logs from a synthetic log producer, classify the logs using a machine learning model into urgency categories, and take appropriate actions based on the level of urgency.

## Nodes Design

### LogProducerNode
This node simulates the production of logs with varying levels of severity. Each log is produced with a unique identifier and a severity level. The node uses the `secrets` module for secure random choices, addressing the cryptographic security issue.

### LogClassifierNode
This node consumes the logs produced by the LogProducerNode and classifies them into urgency categories. The classification is currently simulated using random selection for demonstration purposes, with the `secrets` module used for secure random choices.

### LogActionNode
This node consumes the classified logs and takes action based on the urgency category. Actions range from storing the log for later review to immediate alert and escalation for critical logs.

## Pipeline Configuration
The pipeline is configured with three nodes: LogProducer, LogClassifier, and LogAction. Each node is connected to datasets that act as input and output streams, facilitating the flow of logs through the classification process and resulting in actions being taken.

The datasets are implemented as Kafka streams, allowing for real-time processing and scalability.
