# Fibonacci Processor

## Purpose

The Fibonacci Processor project is designed to generate and process a Fibonacci sequence in real-time. The project utilizes the Aineko framework to create a streaming workflow that continuously computes the next number in the Fibonacci sequence and outputs it to a Kafka stream.

## Design

### Nodes

The project defines a single node, `FibonacciNode`, which is responsible for generating the Fibonacci sequence. It uses two state variables, `a` and `b`, to hold the last two numbers of the sequence. During each execution cycle, the node outputs the current value of `a` and then updates `a` and `b` to the next two numbers in the sequence.

### Pipeline

The pipeline configuration, defined in `pipeline.yml`, sets up the `FibonacciNode` and connects its output to a Kafka stream named `fibonacci_output`. The pipeline is configured to allocate 0.5 CPUs to the node, ensuring efficient resource usage.

## Usage

To use the Fibonacci Processor, deploy the pipeline using the Aineko framework. The node will start generating the Fibonacci sequence, which can be consumed from the `fibonacci_output` Kafka stream for further processing or analysis.