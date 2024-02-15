# Surprise Generator

The Surprise Generator project is designed to provide users with random surprises. The project uses the Aineko framework to create a pipeline that generates a surprise from a predefined list and outputs it to the user.

## Nodes

The `SurpriseNode` is the core component of this project. It selects a surprise from a list of predefined options using a cryptographically secure random choice and writes it to the output dataset.

## Pipeline

The pipeline, `surprise_pipeline`, consists of a single node, `surprise_node`, which is responsible for generating the surprises. The output is written to a Kafka stream dataset named `surprise_output`, which can be consumed by other services or applications to deliver the surprise to the user.

## Design

The design is straightforward, with a focus on simplicity and functionality. The `SurpriseNode` uses Python's `secrets.randbelow` to securely select a surprise, ensuring that the surprises are unpredictable and varied. The pipeline is configured to run continuously, allowing for real-time surprise generation.

## Usage

To use the Surprise Generator, simply run the pipeline and consume the `surprise_output` dataset to receive a random surprise. The project is designed to be easily integrated into larger systems that require a fun and engaging user experience.
