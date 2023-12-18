# DataProcessor

The DataProcessor project is designed to provide a simple yet powerful pipeline for processing streaming data. The pipeline leverages the Aineko framework to create a streaming workflow that can handle real-time data processing.

## Pipeline Design

The pipeline consists of a single node, `DataTransformerNode`, which applies a transformation rule to the incoming data. The transformation rule can be customized as per the requirements. By default, it doubles the input value.

## Nodes

### DataTransformerNode

This node consumes data from the `input_dataset`, applies the transformation rule, and then produces the transformed data to the `output_dataset`. It is designed to be flexible and can be easily adapted to different transformation requirements.

## Pipeline Configuration

The `pipeline.yml` file contains the configuration for the pipeline, including the node settings, datasets, and the transformation rule. The datasets are configured to use Kafka streams, allowing for scalable and reliable data processing.

## Usage

To use the DataProcessor pipeline, ensure that the Kafka streams for `input_dataset` and `output_dataset` are properly set up and that the Aineko framework is installed. Once configured, the pipeline can be executed, and it will process the streaming data according to the specified transformation rule.
