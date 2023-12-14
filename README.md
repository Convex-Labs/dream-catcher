# Hello World Logger

This project contains a simple Aineko pipeline that logs 'Hello World' and then sleeps for 3 seconds. It is designed to demonstrate the basic structure of an Aineko pipeline and node.

## Pipeline Design

The pipeline consists of a single node, `HelloWorldLoggerNode`, which performs the logging and sleeping action. The node is defined in `nodes.py` and is referenced in the `pipeline.yml` configuration file.

## Node Implementation

The `HelloWorldLoggerNode` is a subclass of `AbstractNode` and implements the `_execute` method. Within this method, it uses Python's `logging` module to log 'Hello World' and then calls `sleep` from the `time` module to pause execution for 3 seconds.

## Running the Pipeline

To run the pipeline, ensure that the Aineko framework is properly installed and configured. Then, execute the pipeline using the provided `pipeline.yml` configuration.
