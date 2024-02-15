# Code Generator Project

This project, Code Generator, is designed to generate code snippets based on user prompts using the Aineko framework. The core functionality is encapsulated in a single node, `CodeGeneratorNode`, which takes user prompts as input and produces code as output.

## Design

The `CodeGeneratorNode` uses a predefined template for generating code. The template includes placeholders for a function name, parameters, description, and body. When a user prompt is received, it is used to fill in these placeholders, and the resulting code is produced to the `generated_code` dataset.

## Pipeline

The pipeline, `codegen_pipeline`, is straightforward and consists of the `code_generator` node connected to two datasets: `user_prompt` and `generated_code`. The `user_prompt` dataset acts as the input stream where prompts are received, and the `generated_code` dataset is the output stream where the generated code snippets are sent.

To use the pipeline, users submit their prompts to the `user_prompt` dataset, and the generated code is made available in the `generated_code` dataset. The pipeline is configured in `pipeline.yml`, and the node logic is implemented in `nodes.py`.