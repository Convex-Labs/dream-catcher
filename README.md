# RandomPipeline

## Overview

The RandomPipeline is designed to generate and process random numerical data securely. It consists of two main components: a random number generator that uses a secure generator and a printer that outputs the generated numbers.

## Design

### Nodes

- **RandomNumberGenerator**: This node generates a random integer between 0 and 100 using the `secrets` module, which is designed for cryptographic purposes, ensuring that the random numbers are suitable for security-sensitive applications.

- **RandomNumberPrinter**: This node consumes the random numbers from the `random_numbers` dataset and logs them for visibility.

### Pipeline

The pipeline is configured to use a Kafka stream as the dataset type, allowing for real-time data processing. The `RandomNumberGenerator` node produces data to the `random_numbers` dataset, which is then consumed by the `RandomNumberPrinter` node.

The pipeline is designed to be lightweight and efficient, with each node allocated 0.5 CPUs by default.

## Usage

To run the RandomPipeline, ensure that you have the Aineko framework and Kafka set up. Start the pipeline using the provided configuration file, and observe the logs to see the random numbers being processed in real-time.
