# Fibonacci Generator

## Purpose
The Fibonacci Generator project is designed to generate a Fibonacci sequence using a streaming data pipeline. The project utilizes two nodes within the pipeline to produce and consume the Fibonacci numbers in real-time.

## Design
The pipeline consists of two nodes:

1. `FibonacciProducer`: This node is responsible for generating the Fibonacci sequence. It starts with the first two numbers of the sequence and continuously produces the next number by summing up the two preceding numbers.

2. `FibonacciConsumer`: This node consumes the Fibonacci numbers produced by the `FibonacciProducer`. It logs the consumed numbers and can be extended to perform further processing on the Fibonacci numbers.

The nodes communicate through a Kafka stream dataset named `fibonacci_sequence`, which acts as a buffer for the Fibonacci numbers.

## Pipeline
The pipeline configuration is defined in `pipeline.yml`, which specifies the nodes, their roles (producer/consumer), and the dataset they interact with. The `default_node_settings` provide a default CPU allocation for each node, ensuring efficient resource usage.

To run the pipeline, ensure that the Aineko framework is properly set up and execute the pipeline using the provided configuration file. The nodes will start generating and consuming the Fibonacci sequence in real-time.