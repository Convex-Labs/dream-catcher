# Code Generator Project

This project, Code Generator, is designed to generate code snippets based on user prompts using the Aineko framework. The goal is to automate the creation of code, making it easier for users to get started with their coding tasks.

## Nodes Design

The `CodeGeneratorNode` is the core component of this project. It listens for user prompts on the `user_prompt` dataset and uses a predefined template to generate code. The template is formatted with parameters received from the user prompt, and the resulting code is then produced to the `generated_code` dataset.

## Pipeline Design

The pipeline, `codegen_pipeline`, is configured with a single node, `code_generator`. This node consumes prompts from the `user_prompt` dataset and produces the generated code to the `generated_code` dataset. The node's behavior is defined by the `template` parameter, which specifies the structure of the code to be generated.

The datasets are configured as Kafka streams, allowing for real-time data processing and code generation.
