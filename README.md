# Hello World Project

This project contains a simple Aineko pipeline that outputs 'Hello, World!' to demonstrate the basic functionality of an Aineko pipeline.

## Nodes

The pipeline contains a single node, `HelloWorldNode`, which logs and produces the string 'Hello, World!' to the `output` dataset.

## Pipeline

The pipeline configuration is defined in `pipeline.yml`, which specifies the `HelloWorldNode` and its output dataset. The `output` dataset is of type `kafka_stream`, which allows for real-time data streaming.