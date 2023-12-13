# Math Puzzle Generator

## Purpose

The Math Puzzle Generator project aims to provide an engaging way for students and enthusiasts to practice basic arithmetic operations. It generates random math puzzles that involve addition, subtraction, multiplication, and division.

## Design

The project is built using the Aineko framework, which allows for the creation of a streaming workflow to process data in real-time. The core component of this project is a single node, `MathPuzzleNode`, which is responsible for generating the puzzles.

### MathPuzzleNode

This node operates by randomly selecting two integers between 1 and 100 and a random arithmetic operation (addition, subtraction, multiplication, or division). It then constructs a puzzle string and calculates the answer using `ast.literal_eval`, which is a safe method to evaluate expressions from untrusted sources. The puzzle and its solution are then produced to a Kafka stream dataset, making them available for consumption by other components or services.

## Pipeline

The pipeline configuration is defined in `pipeline.yml`, which sets up the `MathPuzzleNode` and the `math_puzzle` dataset. The node is configured to continuously generate puzzles and stream them to the dataset.

To run the pipeline, ensure that the Aineko framework is properly set up and execute the pipeline using the provided configuration file. The puzzles will be generated and streamed in real-time, ready to be consumed by any application or service integrated with the Kafka stream.

## Conclusion

The Math Puzzle Generator is a simple yet effective tool for creating an endless stream of math puzzles. It demonstrates the power and flexibility of the Aineko framework for building real-time data processing applications.
