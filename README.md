# Fibonacci Generator

## Purpose

The Fibonacci Generator project is designed to create a pipeline that generates and processes a Fibonacci sequence in real-time. The project utilizes two nodes within the Aineko framework to produce and consume the sequence, demonstrating the power of streaming workflows.

## Design

### Nodes

- `FibonacciProducer`: This node initializes the Fibonacci sequence and enters a loop where it continuously calculates the next number in the sequence by summing the last two numbers. The newly calculated number is then produced to the `fibonacci_sequence` dataset. The sequence generation is limited to 100 numbers to prevent infinite execution.

- `FibonacciConsumer`: This node consumes numbers from the `fibonacci_sequence` dataset as they are produced. Upon receiving a number, it logs the number to demonstrate that it has been received and processed.

### Pipeline

The `fibonacci-sequence-pipeline` is configured in `pipeline.yml` and connects the `FibonacciProducer` and `FibonacciConsumer` nodes through the `fibonacci_sequence` dataset. The producer node outputs to this dataset, while the consumer node takes its input from the same dataset, creating a simple yet effective streaming data flow.

The pipeline is designed to be lightweight, with each node allocated 0.5 CPUs by default, ensuring efficient resource utilization.

## Conclusion

This project showcases the simplicity and efficiency of the Aineko framework for real-time data processing. By leveraging the streaming capabilities of Aineko, the Fibonacci Generator project provides a clear example of how to construct a pipeline for generating and consuming a sequence of numbers in real-time.