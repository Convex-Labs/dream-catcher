# Secure Cool Data Stream Project

This project implements a pipeline that processes a simulated data stream securely and in a cool way. The pipeline is built using the Aineko framework and consists of two main components: a secure data simulator and a cool data processor.

## SecureDataSimulatorNode

The `SecureDataSimulatorNode` is responsible for generating simulated data securely. It uses the `secrets` module to produce cryptographically secure random integer values within a specified range and emits them to the `secure_simulated_data_stream` dataset.

## CoolProcessorNode

The `CoolProcessorNode` consumes the secure simulated data from the `secure_simulated_data_stream` dataset and applies a 'cool' transformation to it. In this example, the transformation multiplies the data by 42. The processed data is then emitted to the `cool_data_stream` dataset.

## Pipeline Configuration

The pipeline is configured in `pipeline.yml`, where the nodes and datasets are defined. The `SecureDataSimulatorNode` is set to output to the `secure_simulated_data_stream`, and the `CoolProcessorNode` is set to input from the `secure_simulated_data_stream` and output to the `cool_data_stream`.

The pipeline is designed to be lightweight and efficient, with each node configured to use 0.5 CPUs by default.

## Running the Pipeline

To run the pipeline, ensure that you have the Aineko framework installed and configured. Then, execute the pipeline using the provided configuration file. The pipeline will simulate a data stream securely and process it in real-time, showcasing the power and flexibility of the Aineko framework for streaming data workflows with an emphasis on security.
