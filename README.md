# Restaurant Recommender

## Purpose
The Restaurant Recommender project is an AI agent designed to provide high-quality restaurant recommendations. It leverages the Yelp API to fetch restaurant data and a FAISS vector database to enrich prompts with relevant information. The enriched prompts are then used to interact with an LLM provided by the OpenAI API, utilizing LangChain and Llamaindex for enhanced capabilities.

## Design
The pipeline consists of three main nodes:

1. `YelpDataFetcher`: This node fetches restaurant data from the Yelp API based on user location input. It includes a timeout in the request to ensure the application does not hang if the Yelp API is slow to respond.

2. `FaissIndexer`: This node uses a FAISS vector database to enrich the restaurant data with additional context to improve the quality of the recommendations.

3. `LLMRecommender`: This node interacts with an LLM to generate recommendations based on the enriched data.

Each node is designed to perform a specific task in the recommendation process, ensuring that the final output is a curated list of restaurant suggestions tailored to the user's preferences and context.