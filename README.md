# Email Aggregator Project

## Purpose
The Email Aggregator project is designed to automatically fetch emails from a Gmail account and store them into a database. This can be useful for various applications such as customer support, data analysis, and backup purposes.

## Design
The project consists of two main components:

1. **GmailFetcher Node**: This node uses the Gmail API to retrieve emails from the user's inbox. It decodes the email content and emits it to the `email_content` dataset.

2. **DatabaseWriter Node**: This node consumes the `email_content` dataset and writes the email content to a specified database. It uses SQLAlchemy to interact with the database.

## Pipeline
The pipeline is configured with two nodes: `GmailFetcher` and `DatabaseWriter`. The `GmailFetcher` node outputs to the `email_content` dataset, which is then consumed by the `DatabaseWriter` node to persist the emails into the database.

To run the pipeline, you will need to provide your Gmail API credentials and database connection URL in the `pipeline.yml` file. Ensure that the Gmail API is enabled for your Google Cloud project and that you have the necessary permissions to access the Gmail account and the database.