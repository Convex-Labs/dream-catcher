# TimeSeriesSolver

The TimeSeriesSolver project is designed to solve time series problems using ARIMA and TBATS models. It processes cleaned historical time series data to predict future demand.

## Nodes

The `TimeSeriesPredictor` node is the core of the project. It consumes cleaned historical demand data and uses either the ARIMA or TBATS model to predict future demand. The node can be configured to use a specific model and to output the prediction results as a PNG file.

## Pipeline

The pipeline is configured to use the `TimeSeriesPredictor` node, which takes in cleaned historical demand data and outputs forecasted demand. The pipeline can be easily adjusted to change the model type, sample period, and output file name.

## Design

The design of the nodes and pipeline is focused on flexibility and ease of use. Users can specify the model type and other parameters directly in the pipeline configuration file. The node code is written to be simple and understandable, while still providing powerful time series prediction capabilities.