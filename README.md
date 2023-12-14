# API Load Tester

This project contains an Aineko pipeline designed to simulate load testing on a specified API endpoint. The pipeline is configured to perform a series of requests to the API endpoint to test its ability to handle load.

## Design

The pipeline consists of a single node, `APILoadTester`, which is responsible for executing the load test. The node is configured with parameters such as the API endpoint, request method, total number of requests, concurrency level, and optional throttling between requests.

The `APILoadTester` node uses the Python `requests` library to make HTTP requests to the API. It supports both GET and POST methods and can be configured with custom headers and data payloads for POST requests. The node logs the status code of each response and the number of requests made, providing visibility into the load test progress and the API's response.

## Usage

To use the pipeline, update the `pipeline.yml` file with the desired configuration for the load test. Specify the API endpoint, request method, and other parameters as needed. The pipeline can then be executed using the Aineko framework, which will run the `APILoadTester` node according to the configuration.

The pipeline is designed to be simple and easy to understand, while still providing the necessary functionality to simulate API load testing effectively.

## Updates

Based on the Bandit security analysis, the node code has been updated to include timeouts for the requests to prevent hanging requests and potential denial of service attacks.
