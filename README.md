# Inspirational Quotes Pipeline

This project, Inspirational Quotes, is designed to generate inspirational quotes using a generative language model. The pipeline is built using the Aineko framework and leverages the OpenAI API to produce quotes that can motivate and inspire.

## Design

The pipeline consists of a single node, `QuoteGeneratorNode`, which sends a prompt to the OpenAI API to generate an inspirational quote. The node is configured to receive a prompt and produce a quote as output to the `inspirational_quote` dataset.

The `QuoteGeneratorNode` is implemented in Python and inherits from `AbstractNode`. It uses the OpenAI API's `Completion.create` method to generate quotes based on the provided prompt. The response from the API is then processed to extract the quote, which is subsequently published to the Kafka stream dataset.

## Pipeline Configuration

The pipeline is defined in the `pipeline.yml` file, which specifies the node class and the dataset it produces to. The `inspirational_quote` dataset is of type `kafka_stream`, allowing for real-time streaming of quotes.

## Usage

To use the pipeline, ensure that the OpenAI API key is set in the environment variables as `OPENAI_API_KEY`. Once the pipeline is running, it will continuously generate and stream inspirational quotes to the `inspirational_quote` dataset.

## Conclusion

The Inspirational Quotes project showcases the simplicity and power of the Aineko framework for real-time data processing and streaming. By integrating with the OpenAI API, it provides a scalable solution for generating content that can be used in various applications requiring motivational messages.