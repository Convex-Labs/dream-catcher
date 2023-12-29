# GitHub Crawler Project

This project contains a pipeline that crawls GitHub to create a database of users and projects. The pipeline uses the Aineko framework to periodically fetch data from GitHub's public API and store it in a PostgreSQL database.

## Nodes

### GitHubCrawlerNode

This node is responsible for fetching users and projects from GitHub's API and inserting the data into the database. It handles API pagination and database connection. The requests to the GitHub API are made with a timeout to ensure that the node does not hang indefinitely if the API is unresponsive.

## Pipeline

The pipeline configuration is set up to run the GitHubCrawlerNode with the necessary parameters to connect to the database and to specify a timeout for the requests.

## Database Schema

The database should have two tables: `users` and `projects`. The `users` table stores GitHub user data, and the `projects` table stores GitHub project data with a foreign key linking to the `users` table.

## Usage

To run the pipeline, ensure that the database is set up with the correct schema and that the `database_url` and `request_timeout` in `pipeline.yml` are configured to point to your database instance and desired timeout settings. Then, execute the pipeline using the Aineko CLI.
