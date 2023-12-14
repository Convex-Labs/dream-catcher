# Fibonacci Generator

The Fibonacci Generator project is designed to generate a Fibonacci sequence using a pipeline with two nodes. The sequence is produced by the `FibonacciProducer` node and consumed by the `FibonacciConsumer` node.

## Design

The pipeline consists of two main components:

1. **FibonacciProducer**: This node starts with the first two numbers of the Fibonacci sequence and iteratively produces the next number by summing up the last two numbers in the state. The produced number is sent to the `fibonacci_output` dataset.

2. **FibonacciConsumer**: This node consumes numbers from the `fibonacci_input` dataset and logs the received Fibonacci number. It acts as a sink for the Fibonacci numbers produced by the `FibonacciProducer`.

## Pipeline Configuration

The `pipeline.yml` file contains the configuration for the pipeline, defining the nodes and datasets. The `fibonacci_output` dataset produced by the `FibonacciProducer` is connected to the `fibonacci_input` dataset consumed by the `FibonacciConsumer`. This setup allows the sequence to flow from the producer to the consumer.

The default node settings allocate 0.1 CPUs to each node, ensuring that the pipeline can run efficiently on systems with limited resources.

## Running the Pipeline

To run the pipeline, ensure that the Aineko framework is properly installed and configured. Then, execute the pipeline using the provided `pipeline.yml` configuration. The nodes will start generating and consuming the Fibonacci sequence in real-time.

## Conclusion

The Fibonacci Generator project showcases the simplicity and power of the Aineko framework for creating data streaming pipelines. By leveraging the framework's capabilities, we can easily construct a pipeline that generates and processes a Fibonacci sequence in real-time.