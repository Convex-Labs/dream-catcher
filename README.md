# ChatGPT Pipeline

This project contains a pipeline that interacts with OpenAI's ChatGPT to generate responses based on prompts.

## Design

The pipeline consists of a single node, `ChatGPTNode`, which consumes prompts from the `input_prompt` dataset, queries ChatGPT, and produces the responses to the `gpt_response` dataset.

### ChatGPTNode

The `ChatGPTNode` is responsible for the core functionality of querying ChatGPT. It uses the OpenAI Python client to send prompts to the ChatGPT API and retrieve the generated text. The node is designed to handle a stream of prompts and generate responses in real-time.

### Pipeline Configuration

The `pipeline.yml` file configures the pipeline, defining the input and output datasets, and setting the OpenAI API key as a node parameter. This allows the node to authenticate with the OpenAI API and perform queries.

## Usage

To use the pipeline, prompts should be produced to the `input_prompt` dataset, and the generated responses can be consumed from the `gpt_response` dataset. The pipeline is designed to be scalable and can handle a high throughput of prompts and responses.

## Conclusion

The ChatGPT Pipeline is a simple yet powerful tool for integrating ChatGPT into streaming data applications, enabling real-time interaction with an AI language model.