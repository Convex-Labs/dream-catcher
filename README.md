# GitHub Crawler Project

## Purpose
The GitHub Crawler project is designed to systematically crawl GitHub repositories to create a comprehensive database of users and projects. This enables analysis and insights into open-source project trends, contributor activity, and more.

## Node Design
The `GitHubCrawlerNode` is the core component of this project. It utilizes the PyGithub library to access GitHub's API and iterates over repositories. For each repository, it processes and stores relevant data about the project and its contributors into a database.

## Pipeline Configuration
The pipeline is configured with a single node, `github_crawler`, which is responsible for the crawling process. It is set up with necessary parameters to establish a connection to the database where the crawled data will be stored.

## Usage
To use this project, ensure that the `GITHUB_ACCESS_TOKEN` environment variable is set with a valid GitHub access token. Update the `pipeline.yml` with the correct database connection parameters. Run the pipeline to start crawling GitHub and populating the database.
