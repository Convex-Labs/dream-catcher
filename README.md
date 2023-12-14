# Fibonacci Generator

## Overview

The Fibonacci Generator project is designed to create a sequence of Fibonacci numbers using a simple Aineko pipeline. The pipeline consists of two nodes: a producer and a consumer. The producer node generates the sequence, while the consumer node logs each number as it is produced.

## Nodes

### FibonacciProducer

This node initializes with the first two numbers of the Fibonacci sequence and enters a loop where it produces the next number in the sequence by summing the two previous numbers. The state is then updated with the new pair of numbers for the next iteration.

### FibonacciConsumer

The consumer node listens for new Fibonacci numbers produced by the producer node. Upon receiving a new number, it logs the number to demonstrate that it has been consumed.

## Pipeline Design

The pipeline is configured in `pipeline.yml` and consists of the following components:

- `fibonacci_producer`: The node responsible for generating the Fibonacci sequence.
- `fibonacci_consumer`: The node that consumes and logs each Fibonacci number.
- `fibonacci_sequence`: A Kafka stream dataset that acts as the communication channel between the producer and consumer nodes.

The pipeline is designed to run continuously, producing and consuming an infinite sequence of Fibonacci numbers. The default node settings allocate 0.5 CPUs to each node, ensuring that the pipeline can run efficiently on most systems.
