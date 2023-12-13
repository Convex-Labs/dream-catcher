# Number Doubler Project

## Purpose

The purpose of this project is to demonstrate a simple Aineko pipeline that generates a sequence of numbers and then doubles each number in the sequence. This project serves as an example of how to create and connect nodes within the Aineko framework.

## Design

### Nodes

- `NumberGeneratorNode`: This node starts at a specified number and generates a sequence of numbers up to a defined limit. Each number is produced to the `sequence` dataset.

- `NumberDoublerNode`: This node consumes numbers from the `sequence` dataset, doubles each number, and then produces the result to the `doubled_sequence` dataset.

### Pipeline

The pipeline is configured in `pipeline.yml` and consists of two nodes: `number_generator` and `number_doubler`. The `number_generator` node outputs to the `sequence` dataset, which is then consumed by the `number_doubler` node. The doubled numbers are output to the `doubled_sequence` dataset.

## Usage

To run this pipeline, ensure that the Aineko framework is properly installed and configured. Then, execute the pipeline using the provided `pipeline.yml` configuration. The pipeline will automatically terminate after generating and doubling the sequence of numbers from the specified start to end values.
