# CoolProject

CoolProject is an innovative project that leverages the Aineko framework to do something cool. The project is designed to be a template for real-time data processing using a pipeline of nodes that can be easily extended and customized.

## Nodes Design

The `CoolNode` is the primary node in the CoolProject. It is responsible for implementing the cool functionality that defines the project. The node uses the `_execute` method to perform its main logic, which is executed repeatedly as the pipeline runs.

## Pipeline Design

The pipeline is configured in `pipeline.yml` and consists of the `CoolNode` and a `cool_dataset`. The `CoolNode` is a Python class that inherits from `AbstractNode` and is defined in the `nodes.py` file. The `cool_dataset` is a Kafka stream that acts as a buffer for data that the `CoolNode` can consume from and produce to.

The project is designed to be robust and efficient, ensuring that it can handle real-time data processing without any issues.