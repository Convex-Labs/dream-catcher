# Cool Project

This project, Cool Project, is designed to do something cool. It leverages the Aineko framework to process data in real-time, providing a streaming workflow that is both efficient and scalable.

## Nodes

The `CoolNode` is the core computational unit of this project. It inherits from `AbstractNode` and implements the `_execute` method where the cool functionality is defined. This node can be extended to consume from input datasets and produce to output datasets as needed.

## Pipeline

The pipeline is configured in `pipeline.yml` and consists of the `CoolNode` and a `cool_dataset`. The `cool_dataset` is a Kafka stream that serves as a buffer for data that `CoolNode` can consume from and produce to. The pipeline is named `cool-pipeline` and is designed to be a simple yet powerful example of how to build an Aineko pipeline.
