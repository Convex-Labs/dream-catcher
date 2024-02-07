# Aineko Dream

Aineko Dream is a real-time code generation project that leverages the power of ChatGPT to generate template code based on user prompts. The project uses the Aineko framework to create a pipeline that fetches documentation from GitHub, processes user prompts, queries the OpenAI API, evaluates the generated code for security and validity, and provides the final code to the user.

## Design

The project consists of several nodes:

- `GitHubDocFetcher`: Fetches and updates documentation from a specified GitHub repository.
- `OpenAIClient`: Connects to the OpenAI API to submit prompts and retrieve responses.
- `SecurityEvaluation`: Evaluates the security of the generated code using Bandit.

These nodes are connected through datasets that act as communication channels, ensuring a smooth flow of data and processing steps.

## Pipeline

The pipeline is defined in `pipeline.yml`, where each node is configured with its respective inputs, outputs, and parameters. The datasets are set up to handle the streaming of data between nodes.

By structuring the project as an Aineko pipeline, we can easily modify, extend, or replace parts of the process without affecting the overall functionality. This modularity also allows for easy scaling and maintenance.

## Usage

To use Aineko Dream, users submit prompts to the API server, which are then processed by the pipeline to generate code. The pipeline ensures that the code is not only syntactically correct but also secure and adheres to best practices.

## Conclusion

Aineko Dream showcases the capabilities of the Aineko framework in building complex, real-time processing applications. It demonstrates how generative AI can be integrated into software development workflows to enhance productivity and ensure quality.