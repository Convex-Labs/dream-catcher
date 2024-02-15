# CodeGenAssistant

CodeGenAssistant is an Aineko pipeline designed to generate code based on user prompts. It uses OpenAI's GPT-3 engine to interpret prompts and generate corresponding code snippets.

## Design

The pipeline consists of two main nodes:

1. `PromptHandler`: This node receives user prompts from the `user_prompt` dataset, queries the OpenAI API to generate code, and then sends the generated code to the `generated_code` dataset.

2. `CodeValidator`: This node takes the generated code from the `generated_code` dataset, validates it using Bandit for any security issues, and outputs the validation results to the `validation_result` dataset.

The `user_prompt` dataset acts as the entry point for user prompts, while the `generated_code` and `validation_result` datasets facilitate the flow of data between nodes.

## Usage

To use the CodeGenAssistant, submit a prompt to the `user_prompt` dataset. The generated code will be validated and the results will be available in the `validation_result` dataset. If the code is valid, it can be used as needed. If not, the issues will be detailed in the validation results for further action.