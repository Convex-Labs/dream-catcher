# Fibonacci Generator

## Purpose

The Fibonacci Generator project is designed to generate a Fibonacci sequence using a simple Aineko pipeline. The pipeline consists of two nodes: a producer and a consumer. The producer node generates the sequence, while the consumer node logs each number received.

## Design

### Nodes

- `FibonacciProducer`: This node initializes with the first two numbers of the Fibonacci sequence and enters a loop where it produces the next number in the sequence by summing the two previous numbers. It then updates its state with the new pair of numbers for the next iteration.

- `FibonacciConsumer`: This node consumes the numbers produced by the FibonacciProducer. Upon receiving a new number, it logs the number to demonstrate that it has been received.

### Pipeline

The `fibonacci-sequence-pipeline` is configured in `pipeline.yml`. It defines the nodes and the single dataset `fibonacci_sequence` used for communication between the producer and consumer. The dataset is of type `kafka_stream`, which allows for real-time streaming of the Fibonacci numbers from the producer to the consumer.

## Usage

To run the pipeline, ensure that the Aineko framework is properly installed and configured. Then, execute the pipeline using the provided configuration file. The consumer will log each Fibonacci number as it is produced in real-time.