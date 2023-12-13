# HelloWorld Aineko Project

This project contains a simple Aineko pipeline that demonstrates the basic functionality of an Aineko node by logging 'Hello, World!' to the console.

## Design

The project consists of a single node, `HelloWorldNode`, which inherits from `AbstractNode`. The node overrides the `_execute` method to log 'Hello, World!' whenever it is executed.

## Pipeline

The pipeline configuration, defined in `pipeline.yml`, sets up the `HelloWorldNode` without any inputs or outputs, as it is a standalone node that does not process any data.

To run this pipeline, ensure that you have the Aineko framework installed and execute the pipeline using the Aineko CLI tools.
