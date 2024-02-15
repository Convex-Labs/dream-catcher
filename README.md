# TestProject

TestProject is a simple Aineko pipeline designed for testing purposes. It includes a single node that receives input, logs the input, processes it by appending a 'Tested:' prefix, and then outputs the result.

## Node Design

The `TestNode` is the core computational unit of this project. It inherits from `AbstractNode` and implements the `_execute` method, which is called repeatedly as the pipeline runs. This node reads from the `test_input_dataset`, processes the data, and writes the result to the `test_output_dataset`.

## Pipeline Design

The pipeline is configured in `pipeline.yml` and consists of the `TestNode` and two datasets: `test_input_dataset` and `test_output_dataset`. The `test_input_dataset` acts as the source of data for the `TestNode`, and the `test_output_dataset` is where the processed data is written to.

The pipeline is designed to be simple and easy to understand, providing a basic example of how an Aineko pipeline operates with real-time data processing.