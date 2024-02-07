# NavierStokesSimulator

## Overview
The NavierStokesSimulator is a project designed to simulate the Navier-Stokes equation for fluid dynamics. It takes an input matrix representing the initial state of the fluid and computes the fluid flow based on the viscosity and density parameters.

## Nodes Design
The project contains a single node, `NavierStokesSimulatorNode`, which performs the simulation. It inherits from `AbstractNode` and implements the `_execute` method where the main simulation logic resides. The node consumes an input matrix from the `input_data` dataset, runs the simulation, and produces the result to the `output_data` dataset.

## Pipeline Design
The pipeline is configured in `pipeline.yml` with the `NavierStokesSimulator` node connected to `input_data` and `output_data` datasets. Parameters such as viscosity and density can be adjusted in the node configuration. The datasets are configured to use Kafka streams, allowing for real-time data processing.

## Usage
To run the simulation, provide an input matrix to the `input_data` dataset. The simulator will process the data and output the result to the `output_data` dataset. The pipeline can be scaled and adjusted as needed to accommodate different simulation scenarios.
