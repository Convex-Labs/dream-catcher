# HelloWorld Pipeline

This project contains a simple Aineko pipeline that logs 'Hello, World!' to the console.

## Pipeline Design

The pipeline consists of a single node, `HelloWorldNode`, which is responsible for logging the message to the console. There are no datasets involved in this pipeline as it is a straightforward task that does not require any data to be passed between nodes.

## Running the Pipeline

To run the pipeline, execute the following command:

```bash
aineko run ./conf/pipeline.yml
```

Upon execution, the pipeline will initialize the `HelloWorldNode` and log 'Hello, World!' to the console.

## Conclusion

This project demonstrates the basic setup of an Aineko pipeline with a single node. It serves as an example for creating more complex pipelines using the Aineko framework.