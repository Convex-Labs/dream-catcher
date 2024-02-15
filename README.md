# LLM Fine-Tuner

The LLM Fine-Tuner project is designed to fine-tune a large language model using a pipeline approach. The pipeline consists of three main nodes: DataPreparation, ModelTraining, and ModelEvaluation.

## DataPreparation Node

The DataPreparation node is responsible for preparing the training data. This includes cleaning, tokenizing, and formatting the data to be compatible with the language model's training process.

## ModelTraining Node

The ModelTraining node takes the prepared data and uses it to fine-tune the language model. This involves setting up the training parameters, monitoring the training process, and saving the trained model.

## ModelEvaluation Node

After the model has been trained, the ModelEvaluation node evaluates the performance of the fine-tuned model. This includes running validation tests and generating performance reports.

The pipeline is configured in `pipeline.yml`, and the nodes are implemented in Python within `nodes.py`. The project aims to streamline the fine-tuning process and ensure that the language model is trained effectively and efficiently.
