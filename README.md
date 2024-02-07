# ChatMath Project

## Overview
The ChatMath project is an Aineko pipeline that combines the capabilities of OpenAI's ChatGPT with real-time mathematical operations. The pipeline takes user input, processes it through ChatGPT for natural language understanding, and then performs any mathematical operations specified in the input.

## Nodes
### ChatGPTNode
This node interfaces with OpenAI's ChatGPT to process natural language input and generate responses based on the given prompt.

### MathNode
The MathNode takes a mathematical expression as input, evaluates it using `ast.literal_eval` for safety, and outputs the result. It acts as a real-time calculator within the pipeline, ensuring that only valid Python literals are evaluated.

## Pipeline Design
The pipeline is designed to stream data between two main nodes: ChatGPTNode and MathNode. The input_prompt dataset feeds into ChatGPTNode, which then produces gpt_output. Similarly, math_expression feeds into MathNode, resulting in math_output. Both nodes operate concurrently, allowing for seamless integration of chat and math functionalities.
