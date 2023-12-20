# Ethereum Data Ingestion Project

This project is designed to ingest data from the Ethereum blockchain and store it in a PostgreSQL database. The pipeline is built using the Aineko framework and consists of two main nodes: `EthereumDataFetcher` and `PostgresDataInserter`.

## Nodes

### EthereumDataFetcher

This node connects to an Ethereum node using the Web3.py library and fetches the latest block data. The data is then produced to the `ethereum_data` dataset for consumption by other nodes in the pipeline.

### PostgresDataInserter

This node consumes data from the `ethereum_data` dataset and inserts it into a PostgreSQL database. It establishes a connection to the database and executes an SQL command to insert the block number and hash into a table named `ethereum_blocks`.

## Pipeline

The pipeline is defined in `pipeline.yml` and connects the two nodes using the `ethereum_data` dataset. The `EthereumDataFetcher` node produces data to this dataset, while the `PostgresDataInserter` node consumes the data and inserts it into the database.

To run this pipeline, you will need to provide your own Ethereum node HTTP endpoint and PostgreSQL database credentials in the `pipeline.yml` file.

## Design

The design of the nodes follows the Aineko framework's guidelines for creating streaming workflows. The `EthereumDataFetcher` node acts as a data source, continuously polling the Ethereum blockchain for the latest block. The `PostgresDataInserter` node acts as a data sink, inserting the fetched data into the database. This design allows for real-time processing and storage of blockchain data.

The pipeline can be extended by adding more nodes for additional processing or by connecting to other datasets for further data enrichment.