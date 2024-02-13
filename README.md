# Transcript Summarizer

## Purpose
The Transcript Summarizer project is designed to automate the process of fetching YouTube transcripts, validating user prompts, and summarizing the content. It leverages the capabilities of OpenAI and Langchain libraries to process and summarize large volumes of text data in real-time.

## Nodes Design
- `FastAPIServerNode`: A FastAPI server node that provides endpoints for fetching transcripts and validating prompts. It is configured to run on the local interface to avoid binding to all interfaces, addressing potential security concerns.
- `TranscriptFetcherNode`: This node is responsible for fetching transcripts from YouTube based on a provided URL.
- `PromptValidatorNode`: Validates the user prompts to ensure they are in the correct format and contain valid information before processing.
- `TranscriptSummarizerNode`: Utilizes the Langchain library to summarize the fetched YouTube transcript.

## Pipeline Design
The pipeline is configured to process streaming data through Kafka topics, with each node performing its designated task. The `TranscriptFetcherNode` fetches the transcript and passes it to the `TranscriptSummarizerNode` for summarization. The `PromptValidatorNode` ensures that user prompts are valid before any processing occurs. The `FastAPIServerNode` facilitates interaction with the pipeline through HTTP requests.

To run the pipeline, ensure that all dependencies are installed and the Kafka service is up and running. The FastAPI server can be accessed at `http://localhost:8000` after starting the pipeline.
