# Chatbot Project

This project contains a simple chatbot implemented using the Aineko framework. The chatbot is designed to receive messages from an input dataset, process them, and send responses to an output dataset.

## Design

The chatbot is implemented as a single node within the Aineko pipeline. It uses the `ChatbotNode` class, which contains the main logic for handling incoming messages and generating responses.

The `ChatbotNode` listens to the `input_dataset` for new messages. When a new message is received, the `generate_response` method is called to create a response based on the input. The response is then sent to the `output_dataset`.

The pipeline is configured in `pipeline.yml`, which specifies the input and output datasets, as well as the node class to be used.

## Usage

To use the chatbot, messages should be sent to the `input_dataset`, and responses can be read from the `output_dataset`. The chatbot currently echoes the received messages with a simple prefix 'Echo: '.

Future improvements may include more complex response generation logic, integration with natural language processing libraries, or external APIs to create a more interactive and intelligent chatbot experience.
