# Fibonacci Generator

This project implements a simple pipeline that generates a Fibonacci sequence using two nodes within the Aineko framework.

## Purpose

The purpose of this project is to demonstrate the generation of a Fibonacci sequence in a streaming fashion. The pipeline consists of two nodes: a producer and a consumer. The producer node generates the sequence, while the consumer node logs each number for monitoring or further processing.

## Design

### Nodes

- `FibonacciProducer`: This node starts with the initial two numbers of the Fibonacci sequence and continuously produces the next number in the sequence by summing the two previous numbers. The state of the node is maintained to keep track of the sequence.

- `FibonacciConsumer`: This node consumes the Fibonacci numbers produced by the `FibonacciProducer` and logs them. This demonstrates how a node can act as a consumer within a pipeline.

### Pipeline

The `pipeline.yml` file configures the pipeline, defining the nodes and the dataset used for communication between them. The `fibonacci_sequence` dataset acts as a Kafka stream, which the producer writes to and the consumer reads from.

## Running the Pipeline

To run the pipeline, ensure that the Aineko framework is properly set up and that Kafka is running as the message broker. Then, execute the pipeline using the provided configuration file.

## Conclusion

This project showcases a simple yet effective use of the Aineko framework to generate and process a Fibonacci sequence in real-time. By leveraging the streaming capabilities of Aineko, we can efficiently produce and consume data in a distributed system.