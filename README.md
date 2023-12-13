# Number Processor

## Purpose

The Number Processor project is designed to generate a sequence of numbers and then double each number in the sequence. This project is implemented using the Aineko framework and consists of two primary nodes: the Number Generator and the Number Doubler.

## Nodes Design

### Number Generator Node

The Number Generator Node is responsible for creating a sequence of numbers starting from a defined initial value up to an end value. The node will output each number in the sequence to the `number_sequence` dataset.

### Number Doubler Node

The Number Doubler Node consumes the sequence of numbers from the `number_sequence` dataset. Upon receiving a number, it doubles the value and then produces the result to the `doubled_numbers` dataset.

## Pipeline Configuration

The pipeline is configured in `pipeline.yml` and defines the flow of data between the nodes and datasets. The `number_generator` node produces to the `number_sequence` dataset, which is then consumed by the `number_doubler` node. The doubled numbers are then produced to the `doubled_numbers` dataset.

The pipeline is designed to be efficient and scalable, utilizing the Aineko framework's streaming capabilities for real-time data processing.

## Usage

To run the pipeline, ensure that the Aineko framework is installed and configured correctly. Then, execute the pipeline using the provided `pipeline.yml` configuration. The pipeline will automatically terminate once the number sequence generation is complete.
