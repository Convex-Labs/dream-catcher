# Party Planner Project

The Party Planner project is an application designed to plan and organize parties efficiently. It automates the process of receiving party requests and confirming the planning details.

## Nodes Design

The project includes a `PartyPlannerNode` which is responsible for processing incoming party requests. It reads the requests from a Kafka stream, adds them to a JSON file for persistence, and then produces a confirmation message to another Kafka stream.

## Pipeline Design

The pipeline is configured with a single node, `PartyPlanner`, which consumes `party_requests` and produces `party_confirmations`. The node uses a JSON file (`party_data.json`) to store and manage party requests. The pipeline is designed to handle real-time party planning requests and confirmations.

To run the pipeline, ensure that Kafka is set up and the topics `party_requests` and `party_confirmations` are created. The node will process requests as they come in and update the party data file accordingly.
