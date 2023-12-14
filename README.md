# Fibonacci Generator

## Purpose

The Fibonacci Generator project is designed to create a simple yet effective pipeline that generates and processes a Fibonacci sequence in real-time. The project utilizes the Aineko framework to set up a streaming workflow with two nodes: a producer and a consumer.

## Design

### Nodes

- **FibonacciProducer**: This node starts with the initial two numbers of the Fibonacci sequence (0 and 1) and continuously produces the next number in the sequence by summing up the two previous numbers. The produced numbers are sent to a Kafka stream dataset named `fibonacci_sequence`.

- **FibonacciConsumer**: This node consumes the Fibonacci numbers from the `fibonacci_sequence` dataset as they are produced. It logs each number received, demonstrating a simple processing task that could be replaced with more complex logic as needed.

### Pipeline

The `pipeline.yml` configuration file defines the pipeline named `fibonacci-sequence-pipeline`. It sets up the two nodes and the Kafka stream dataset that connects them. The producer node generates the sequence, and the consumer node processes each number. The default node settings allocate 0.5 CPUs to each node, ensuring that the pipeline can run efficiently on systems with limited resources.

## Usage

To run the Fibonacci Generator pipeline, ensure that the Aineko framework is properly installed and configured. Then, execute the pipeline using the provided `pipeline.yml` configuration. The pipeline will start generating and logging the Fibonacci sequence in real-time.