# ChatMath Project

The ChatMath project is an Aineko pipeline that integrates ChatGPT with mathematical operations. It is designed to take an input prompt, generate a response using ChatGPT, and perform mathematical operations on expressions.

## Nodes

### ChatGPTNode

The `ChatGPTNode` is responsible for sending prompts to the ChatGPT service and receiving the generated text. It consumes prompts from the `input_prompt` dataset and produces responses to the `chatgpt_response` dataset.

### MathNode

The `MathNode` takes mathematical expressions from the `math_expression` dataset, evaluates them using `ast.literal_eval` for safe evaluation, and sends the results to the `math_result` dataset. It handles basic mathematical operations and ensures that any errors in evaluation are caught and reported.

## Pipeline

The pipeline is configured with two main nodes: `chatgpt` and `math`. The `chatgpt` node interacts with the ChatGPT service, while the `math` node performs mathematical operations. Both nodes are connected to their respective input and output datasets, allowing for a seamless flow of data and processing within the pipeline.

To run the pipeline, ensure that the Kafka streams for the datasets are properly set up and that the OpenAI API key is correctly configured for the ChatGPT node.