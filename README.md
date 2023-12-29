# Email Aggregator Project

The Email Aggregator project is designed to collect emails from a Gmail account and store them into a database for aggregation and analysis. This project uses the Aineko framework to create a pipeline that fetches emails and writes them to a specified database.

## Nodes Design

### GmailFetcher

The `GmailFetcher` node is responsible for connecting to the Gmail API and retrieving emails from the user's inbox. It uses OAuth2 credentials to authenticate and access the Gmail account. The node fetches the list of emails and for each email, retrieves the subject and body, decodes the body from base64, and sends the data to the `email_data` dataset.

### DatabaseWriter

The `DatabaseWriter` node takes the email data from the `email_data` dataset and writes it to a database. It uses SQLAlchemy to connect to the database and perform the insert operation. The node expects the database URL to be provided in the node parameters.

## Pipeline Configuration

The pipeline is defined in the `pipeline.yml` file, which specifies the nodes, their parameters, and the datasets they interact with. The `GmailFetcher` node is set up with the necessary parameters to authenticate with the Gmail API, and the `DatabaseWriter` node requires the database URL to connect and write data.

To run this pipeline, you will need to provide your Gmail API credentials and database URL in the `pipeline.yml` file. Once configured, the pipeline can be executed to start aggregating emails into your database.

## Conclusion

This Email Aggregator project showcases the power of the Aineko framework in building data pipelines. By leveraging nodes to perform specific tasks, we can create a streamlined process for collecting and storing email data efficiently.