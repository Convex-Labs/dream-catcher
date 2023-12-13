# Cool Math Solver

## Purpose

The Cool Math Solver project is designed to solve arithmetic problems in real-time. It utilizes the Aineko framework to process and evaluate mathematical expressions, providing solutions as output.

## Design

### Nodes

The project consists of a single node, `CoolMathProblemSolver`, which is responsible for solving the math problem provided to it. This node takes an arithmetic expression as input, evaluates it using `ast.literal_eval` for security, and produces the solution to a designated output dataset.

### Pipeline

The pipeline configuration is defined in `pipeline.yml`. It specifies the `CoolMathProblemSolver` node, the input parameters for the math problem to be solved, and the output dataset where the solution will be published.

The pipeline is designed to be lightweight and efficient, with a default setting of 0.5 CPUs allocated to the node to ensure resource-efficient computation.

## Usage

To use the Cool Math Solver, simply provide an arithmetic expression as the `problem` parameter in the `node_params` section of the `pipeline.yml` file. The node will then process the expression safely with `ast.literal_eval` and output the solution to the `math_solution` dataset.

