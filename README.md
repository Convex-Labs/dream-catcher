# API Load Tester

The API Load Tester project is designed to simulate load testing for an API. It uses the Aineko framework to create a pipeline that sends a specified number of requests to a target API endpoint, allowing users to measure the performance and robustness of the API under load.

## Design

The project consists of a single node, `APILoadTester`, which is responsible for generating the API requests. The node is configurable, allowing users to specify the target URL, the number of requests to send (`request_count`), the level of concurrency (`concurrency_level`), the interval between requests (`request_interval`), and the timeout for each request (`timeout`).

The `APILoadTester` node sends GET requests to the specified target URL and produces a stream of responses to the `api_responses` dataset. Each response includes the HTTP status code and the response time, which can be used to analyze the API's performance. In case of request failures, errors are logged with an appropriate error message.

## Pipeline

The pipeline configuration is defined in `pipeline.yml`. It sets up the `load_tester` node with the necessary parameters and connects it to the `api_responses` dataset. The default node settings allocate 1 CPU to the node, ensuring that it has enough resources to perform the load test.

To run the pipeline, users must set the `target_url` to the API endpoint they wish to test. They can also adjust the `request_count`, `concurrency_level`, `request_interval`, and `timeout` to simulate different levels of load.

## Usage

To use the API Load Tester, simply configure the `pipeline.yml` with the desired parameters and run the pipeline using the Aineko framework. The output will be a stream of API response data that can be analyzed to understand the API's behavior under load.

This project is an example of how the Aineko framework can be used to build practical tools for API performance testing. It is simple, easy to understand, and fully expresses the required functionality for simulating API load testing.