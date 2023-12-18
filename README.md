# Package Monitoring Project

This project implements a pipeline using the Aineko framework to monitor IoT device data from packages during shipment. The pipeline aggregates location and handling data from the devices and uses models to generate alerts for potential crashes or theft incidents.

## Design

The pipeline consists of two main nodes:

1. `IoTDataSimulator`: This node simulates the data streams from IoT devices placed within packages. It generates random location and handling metrics within specified ranges to mimic real-world scenarios. The node uses the `secrets.SystemRandom` class for generating random numbers, which is suitable for security purposes.

2. `AlertGenerator`: This node consumes the simulated data and applies thresholds to detect crash or theft incidents. If any data point exceeds the predefined thresholds, an alert is generated and emitted.

## Pipeline Configuration

The `pipeline.yml` file defines the pipeline configuration, including the nodes, their parameters, and the datasets they interact with. The IoT data is streamed through a Kafka topic, allowing for real-time processing and alert generation.

## Usage

To run the pipeline, ensure that the Aineko framework is set up correctly and that the Kafka streams are configured. Start the pipeline using the Aineko CLI, and it will begin monitoring the data and generating alerts as defined by the node logic.

## Future Work

The current implementation uses synthetic data and simple threshold-based models for alert generation. Future enhancements could include integrating machine learning models for more accurate detection and incorporating additional data sources for comprehensive monitoring.
