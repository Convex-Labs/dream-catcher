# Number Sequencer Project

## Purpose

The Number Sequencer project is designed to generate a sequence of numbers using the Aineko framework. It consists of two primary nodes: one for generating the sequence and another for doubling each number in the sequence. This project demonstrates the simplicity and power of Aineko for stream processing tasks.

## Nodes Design

### NumberGeneratorNode

The `NumberGeneratorNode` is responsible for generating a sequence of numbers from a specified start to an end. It uses the `_pre_loop_hook` to initialize the sequence and the `_execute` method to emit each number to the `sequence` dataset until the end of the sequence is reached. Once the sequence is complete, it activates the poison pill to gracefully shut down the pipeline.

### NumberDoublerNode

The `NumberDoublerNode` consumes numbers from the `sequence` dataset, doubles each number, and then produces the result to the `doubled_sequence` dataset. It listens for new data on the `sequence` dataset and processes each message as it arrives.

## Pipeline Configuration

The `pipeline.yml` file defines the configuration of the pipeline, including the nodes and datasets. The `number_generator` node generates the sequence, and the `number_doubler` node doubles the numbers. Both nodes are connected through the `sequence` dataset, which acts as a message channel between them. The `doubled_sequence` dataset is used to hold the output of the `number_doubler` node.

## Running the Project

To run the project, ensure that the Aineko framework is installed and configured correctly. Update the `pipeline.yml` with the desired range for the number sequence and the allocated resources for each node. Execute the pipeline using the Aineko CLI tools, and monitor the output on the `doubled_sequence` dataset.

## Conclusion

The Number Sequencer project is a straightforward example of how to use the Aineko framework for creating data processing pipelines. By following the provided code and configuration, one can quickly set up a streaming pipeline for real-time data processing tasks.
