# CoolProject

CoolProject is a project that does something cool. It's designed to showcase the power of the Aineko framework by implementing a simple yet effective pipeline that increments a number and logs the state.

## Nodes

The `CoolNode` is the core of CoolProject. It initializes with a state and increments this state in each execution cycle. The updated state is then produced to the `cool_output` dataset.

## Pipeline

The pipeline, `cool_pipeline`, is configured to run the `CoolNode` and uses a Kafka stream as the dataset for output. It's a simple example of how Aineko can be used to build event-driven applications.