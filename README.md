# Cat Motivator

The Cat Motivator project is designed to generate cat-themed motivational messages every 3 seconds. This project uses the Aineko framework to create a pipeline that streams these messages.

## Purpose

The purpose of this project is to provide a continuous stream of motivational messages with a fun cat theme. It's intended to be used in applications that require a regular injection of positivity, such as dashboards, mobile apps, or websites.

## Design

The pipeline consists of a single node, `CatMotivatorNode`, which is responsible for generating the messages. The node maintains a list of predefined motivational messages and cycles through them, outputting one message every 3 seconds.

The messages are produced to a Kafka stream dataset named `cat_motivation`, which can be consumed by other components or services within the Aineko ecosystem.

## Pipeline

The pipeline configuration is defined in `pipeline.yml`, which sets up the `cat_motivator` node and the `cat_motivation` dataset. The node is configured with minimal CPU resources, as the task is lightweight.

The `nodes.py` file contains the implementation of `CatMotivatorNode`, which includes a `_pre_loop_hook` method for initializing the messages and an `_execute` method that contains the logic for producing messages to the Kafka stream.

## Usage

To use the Cat Motivator pipeline, deploy it within an Aineko-compatible environment with Kafka set up. Once the pipeline is running, it will automatically start generating and streaming motivational messages every 3 seconds.

Enjoy the stream of cat-themed positivity!