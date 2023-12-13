# Number Doubler Project

## Purpose

The purpose of this project is to demonstrate a simple Aineko pipeline that generates a sequence of numbers and then doubles each number in the sequence. This is achieved through two nodes: `NumberGeneratorNode` and `NumberDoublerNode`.

## Design

### Nodes

- `NumberGeneratorNode`: This node starts at a specified number and generates a sequence of numbers up to a defined limit. Each number is then sent to the `sequence` dataset.

- `NumberDoublerNode`: This node consumes numbers from the `sequence` dataset, doubles each number, and then sends the result to the `doubled_sequence` dataset.

### Pipeline

The pipeline is configured in `pipeline.yml` and consists of the two nodes described above along with their respective datasets. The `NumberGeneratorNode` produces a sequence of numbers which are then consumed by the `NumberDoublerNode` to produce the doubled values.

The datasets `sequence` and `doubled_sequence` are implemented as Kafka streams, allowing for real-time processing of the data.

## Usage

To run this pipeline, ensure that the Aineko framework is installed and configured correctly. Then, execute the pipeline using the provided `pipeline.yml` configuration. The nodes will automatically perform their tasks according to the pipeline's logic.