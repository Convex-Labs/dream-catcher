# Math Solver Pipeline

This project, Math Solver, is designed to solve an interesting math problem using a pipeline composed of three nodes. The pipeline is built using the Aineko framework and is structured to perform a sequence of operations on a number.

## Pipeline Design

The pipeline consists of the following nodes:

1. `NumberGeneratorNode`: This node is responsible for generating a number that will be used as the input for the math problem. It can be configured to start with any number by setting the `start_number` parameter in the pipeline configuration.

2. `MathOperationNode`: The core node where a math operation is performed on the input number. The operation can be any Python function that takes a single argument. It is configured in the pipeline to use `math.pow` function to raise the number to a power, which is specified by the `exponent` parameter.

3. `ResultCollectorNode`: This node collects the result of the math operation and logs it. The result is simply printed out for demonstration purposes.

## Node Implementation

Each node is implemented as a subclass of `AbstractNode` from the Aineko framework. The nodes override the `_execute` method to perform their specific tasks:

- `NumberGeneratorNode` produces a starting number.
- `MathOperationNode` consumes the generated number, applies a math operation, and produces the result.
- `ResultCollectorNode` consumes the result and logs it.

## Running the Pipeline

To run the pipeline, ensure that the Aineko framework is properly set up and the Kafka streams are configured as per the `pipeline.yml` file. Start the pipeline using the Aineko CLI, and it will execute the defined math problem, logging the result to the console.

## Conclusion

The Math Solver pipeline is a simple yet powerful example of how the Aineko framework can be used to construct and execute a data processing pipeline. By adjusting the parameters in the `pipeline.yml` file, different math problems can be solved using the same pipeline structure.