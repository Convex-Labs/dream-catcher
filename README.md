# ChatMath Project

The ChatMath project is designed to leverage the capabilities of ChatGPT to generate math-related content. The project consists of a pipeline that receives math problems, uses ChatGPT to solve them, and outputs the solutions.

## Nodes Design

The `MathChatNode` is the core component of the pipeline. It consumes math problems from the `math_problems` dataset, sends them to ChatGPT with a prompt to solve the problem, and then produces the solution to the `math_solutions` dataset.

## Pipeline Design

The pipeline is configured with a single node, `math_chat`, which is responsible for the interaction with ChatGPT. The node takes in math problems and outputs solutions, facilitating a seamless flow of data from input to output through the ChatGPT model.

The datasets `math_problems` and `math_solutions` are Kafka streams that serve as the input and output channels for the node, respectively.

## Usage

To use the ChatMath pipeline, math problems should be sent to the `math_problems` dataset, and the solutions can be retrieved from the `math_solutions` dataset. The pipeline handles the processing and interaction with ChatGPT internally, providing an easy-to-use interface for generating math-related content.
