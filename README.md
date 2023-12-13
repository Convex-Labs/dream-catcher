# HelloWorld Aineko Project

This project contains a simple Aineko pipeline that demonstrates the basic functionality of an Aineko node. The pipeline consists of a single node that logs 'Hello, World!' to the console.

## Pipeline Design

The pipeline is defined in `pipeline.yml` and consists of a single node named `HelloWorld`. This node is implemented in the `nodes.py` file and is derived from the `AbstractNode` class provided by the Aineko framework.

### HelloWorldNode

The `HelloWorldNode` is a simple node that overrides the `_execute` method from the `AbstractNode` class. In its execution, it logs 'Hello, World!' to the console. This node does not interact with any datasets, making it a standalone operation within the pipeline.

## Running the Pipeline

To run the pipeline, ensure that you have the Aineko framework installed and configured correctly. Then, execute the pipeline using the Aineko CLI with the provided `pipeline.yml` configuration.

```bash
aineko run pipeline.yml
```

You should see 'Hello, World!' logged to the console upon the execution of the pipeline.

## Conclusion

This project serves as a basic example of how to set up and run a minimal Aineko pipeline. It can be used as a starting point for more complex pipelines that involve data processing and interactions between multiple nodes and datasets.
