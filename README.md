# Aineko Dream

Aineko Dream is a real-time code generation system that leverages a large language model (LLM) with built-in quality assurance to ensure the generated code meets quality standards.

## Purpose

The project aims to streamline the code generation process by integrating LLMs to automatically generate code snippets based on user prompts. The quality assurance node ensures that the generated code is error-free and adheres to predefined standards.

## Design

The system is designed around three main nodes:

1. `GitHubDocFetcher`: This node fetches the latest documentation or project descriptions from a specified GitHub repository to use as context for the LLM.

2. `LLMQueryNode`: This node sends prompts to the LLM and receives the generated code.

3. `QualityAssuranceNode`: This node performs quality checks on the generated code. If errors are detected, it reformulates the prompt to correct the errors and sends it back to the LLMQueryNode.

The pipeline is configured to ensure a smooth flow of data between these nodes, with the final output being error-free code snippets ready for use.