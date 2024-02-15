# HelloWorld Pipeline

This project contains a simple Aineko pipeline that outputs 'Hello, World!' to demonstrate the basic functionality of an Aineko node and pipeline configuration.

## Design

The pipeline consists of a single node, `HelloWorldNode`, which logs and produces the string 'Hello, World!' to the `output` dataset.

## Pipeline

The `pipeline.yml` file configures the pipeline with the `hello_world_node` and the `output` dataset. The `HelloWorldNode` is implemented in the `nodes.py` file and is responsible for the core functionality of the pipeline.

## Usage

To run this pipeline, ensure that you have Aineko set up and configured properly. Then, execute the pipeline using the provided `pipeline.yml` configuration.
