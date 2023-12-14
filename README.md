# API Load Tester

## Overview
The API Load Tester project is designed to simulate load testing on a specified API endpoint. It allows you to configure the endpoint, request method, data, headers, and the intensity of the load test.

## Nodes

### APILoadTester
This node is responsible for sending requests to the API endpoint. It supports GET and POST methods and can be configured to send a specific number of requests with a specified delay between each request. A timeout is set for each request to prevent hanging.

## Pipeline
The pipeline is configured to use the `APILoadTester` node to perform the load test. The `poison_pill` dataset is used to gracefully terminate the load test if needed.

## Configuration
You can configure the pipeline by editing the `pipeline.yml` file. Set the `api_endpoint`, `request_method`, `request_data`, `request_headers`, `total_requests`, `time_between_requests`, and `timeout` to match your load testing requirements.

## Execution
To execute the load test, run the pipeline using the Aineko framework. Monitor the logs to see the status of each request and the overall progress of the load test.

## Termination
To terminate the load test before it completes, produce a message to the `poison_pill` dataset. This will trigger the `APILoadTester` node to stop sending requests and exit.

