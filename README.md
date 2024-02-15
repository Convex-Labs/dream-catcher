# Math Solver Project

This project, Math Solver, is designed to solve basic math problems in real-time. It uses the Aineko framework to define a pipeline that processes math problems as they come in and provides solutions.

## Nodes

The `MathSolverNode` is the core component of this project. It consumes math problems from the `math_problem` dataset, safely evaluates them as Python literals using `ast.literal_eval`, and produces the results to the `solution` dataset.

## Pipeline

The pipeline is configured in `pipeline.yml` and consists of a single node, `MathSolver`, which is responsible for solving the math problems. The `math_problem` dataset acts as the input where math problems are received, and the `solution` dataset is where the solutions are sent.

## Design

The design is straightforward, with the node performing the computation and the pipeline managing the flow of data. The node uses Python's `ast` module to safely evaluate the math expressions without executing arbitrary code.