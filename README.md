# DataCategorizer

The DataCategorizer project is designed to ingest data from a database and categorize it using machine learning. The project uses the Aineko framework to create a pipeline that consists of two main nodes: DataIngestion and DataCategorization.

## Nodes

### DataIngestionNode
This node is responsible for connecting to the database and fetching the raw data. It outputs the data to the `raw_data` dataset for further processing.

### DataCategorizationNode
This node consumes the raw data, preprocesses it, and then uses a machine learning model to categorize the data. It splits the data into training and test sets, trains a RandomForestClassifier, and evaluates its accuracy. The categorized data and model accuracy are then produced to the `categorized_data` dataset.

## Pipeline
The pipeline configuration is defined in `pipeline.yml`, which sets up the flow of data between the nodes and datasets. The `DataIngestion` node outputs to the `raw_data` dataset, which is then consumed by the `DataCategorization` node. The categorized data is output to the `categorized_data` dataset.

The project is designed to be modular and scalable, allowing for easy integration with different databases and machine learning models as needed.