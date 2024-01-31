# Fibonacci Generator

The Fibonacci Generator project is designed to generate a Fibonacci sequence using a simple two-node Aineko pipeline. The purpose of this project is to demonstrate the use of Aineko framework for streaming data processing.

## Nodes Design

### FibonacciProducer
The `FibonacciProducer` node is responsible for generating the Fibonacci sequence. It starts with two initial numbers, 0 and 1, and iteratively produces the next number in the sequence by summing the two previous numbers. The node will produce a predefined number of Fibonacci numbers before activating the poison pill to gracefully shut down the pipeline.

### FibonacciConsumer
The `FibonacciConsumer` node consumes the Fibonacci numbers produced by the `FibonacciProducer`. As it receives each number, it logs the number to demonstrate the consumption of the sequence.

## Pipeline Configuration

The `pipeline.yml` file configures the pipeline with the two nodes and a Kafka stream dataset. The `FibonacciProducer` node is set to output to the `fibonacci_sequence` dataset, and the `FibonacciConsumer` node is set to input from the same dataset. This configuration allows the sequence to be passed from the producer to the consumer in real-time.

## Usage

To run the Fibonacci Generator pipeline, ensure that the Aineko framework is properly installed and configured. Then, execute the pipeline using the provided `pipeline.yml` configuration. The consumer will log each Fibonacci number as it is produced by the producer node, demonstrating a simple streaming data pipeline.