# LogSimulator Project

## Purpose
The LogSimulator project is designed to simulate machine logs and process them in real-time. This project is useful for testing log monitoring systems, log analysis algorithms, and for training purposes.

## Design
The project consists of two main components:

1. **LogGeneratorNode**: This node simulates the generation of logs. It creates random log messages at a specified interval and sends them to the `log_stream` dataset. The randomness is improved by using `os.urandom` to generate a secure random number.

2. **LogProcessorNode**: This node consumes the simulated logs from the `log_stream` dataset, processes them, and outputs the results to the `processed_log_stream` dataset. The processing logic can be customized based on the use case.

## Pipeline
The pipeline is configured in `pipeline.yml` and connects the LogGeneratorNode and LogProcessorNode using Kafka streams. The `log_stream` dataset acts as the intermediary between the two nodes, allowing for a decoupled and scalable architecture.

To run the pipeline, ensure that the Aineko framework is properly set up and execute the pipeline configuration using the appropriate Aineko CLI commands.
