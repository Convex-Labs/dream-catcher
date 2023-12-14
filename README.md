# Inventory Manager

## Overview

The Inventory Manager is a simple Aineko pipeline project that simulates inventory updates for a set of items. It uses the Aineko framework to create a streaming workflow that continuously processes simulated inventory data.

## Nodes

### InventorySimulator

The `InventorySimulator` node is responsible for simulating inventory updates. It uses the `secrets` module to generate random inventory adjustments, ensuring that the random number generation is suitable for security purposes. It then updates the inventory count for each item and produces these updates to the `inventory_updates` dataset.

### InventoryLogger

The `InventoryLogger` node consumes updates from the `inventory_updates` dataset and logs the changes. This node acts as a simple observer of the inventory changes and could be extended to persist changes to a database or trigger alerts based on inventory levels.

## Pipeline

The pipeline is configured in `pipeline.yml` and consists of the two nodes described above. The `InventorySimulator` node starts with an initial inventory, which it updates randomly at each execution step. The `InventoryLogger` node listens for these updates and logs them.

The pipeline is designed to be lightweight and easily modifiable to suit different inventory management scenarios. It demonstrates the power of the Aineko framework for building real-time data processing applications.