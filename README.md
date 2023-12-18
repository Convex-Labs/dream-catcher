# DataProcessor Project

## Purpose

The DataProcessor project is designed to provide a simple yet effective pipeline for processing streaming data. The pipeline is built using the Aineko framework and consists of two main components: a data transformer and a data sink.

## Nodes Design

### DataTransformer Node

The `DataTransformer` node is responsible for applying a transformation rule to each piece of data it receives from the input stream. The transformation rule can be customized according to the project's needs. By default, it doubles the input value. The transformed data is then sent to the output stream.

### DataSink Node

The `DataSink` node acts as the endpoint of the pipeline. It receives transformed data from the output stream and typically would write this data to a persistent storage system. For demonstration purposes, this node simply logs the received data.

## Pipeline Configuration

The pipeline is configured in `pipeline.yml`, where `data_transformer` and `data_sink` are defined as the nodes of the pipeline. The `input_stream` and `output_stream` datasets are configured as Kafka streams, facilitating the flow of data through the pipeline.

The `default_node_settings` specify that each node in the pipeline should use 0.5 CPUs, ensuring efficient resource utilization.

## Running the Pipeline

To run the DataProcessor pipeline, ensure that the Aineko framework is properly installed and configured. Then, execute the pipeline using the provided `pipeline.yml` configuration file. The pipeline will automatically start processing data as it arrives in the input stream and will log the output for verification purposes.
