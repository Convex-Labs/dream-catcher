# HelloWorld Aineko Project

This project is a simple demonstration of the Aineko framework, implementing a 'Hello World' pipeline.

## Purpose

The purpose of this project is to showcase the basic setup and execution of an Aineko pipeline that logs 'Hello, World!' to the console.

## Design

### Nodes

The `HelloWorldNode` is a simple node that inherits from `AbstractNode`. It overrides the `_execute` method to log 'Hello, World!' to the console using the inherited `self.log` method.

### Pipeline

The pipeline configuration in `pipeline.yml` defines a single node, `hello_world_node`, which uses the `HelloWorldNode` class from the `hello_world.nodes` module. It is allocated a small fraction of CPU resources, demonstrating how to specify resource requirements for nodes in the Aineko framework.

## Execution

To run this pipeline, ensure that the Aineko framework is properly installed and configured. Then, execute the pipeline using the appropriate Aineko CLI commands.
