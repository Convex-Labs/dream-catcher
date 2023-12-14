# API Load Tester

The API Load Tester project is designed to simulate a load test for an API. It uses the Aineko framework to create a pipeline that sends a series of requests to a specified API endpoint and records the response status and timing.

## Design

The project consists of a single node, `APILoadTester`, which is responsible for executing the load test. The node sends a configurable number of requests to the API endpoint at a specified interval and produces the results to the `api_responses` dataset.

The `APILoadTester` node is defined in `nodes.py` and is configured in `pipeline.yml` with parameters such as `api_url`, `request_count`, `request_interval`, and `timeout`.

## Pipeline

The pipeline configuration in `pipeline.yml` sets up the `load_tester` node and the `api_responses` dataset. The `load_tester` node uses the `APILoadTester` class from `nodes.py` and outputs to the `api_responses` dataset, which is of type `kafka_stream`.

## Usage

To run the load test, ensure that the Aineko framework is set up and the `pipeline.yml` is configured with the correct API endpoint and desired test parameters. Start the pipeline, and the `APILoadTester` node will begin sending requests to the API and producing response data to the `api_responses` dataset.

The results can be monitored in real-time or analyzed after the test to assess the API's performance under load.