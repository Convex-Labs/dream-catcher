from aineko.core.node import AbstractNode
from typing import Optional
import openai
import requests
from langchain.llamas import OpenAICompletion
from llamaindex import FaissIndex

openai.api_key = 'your-openai-api-key'

# Define your nodes here

class YelpDataFetcher(AbstractNode):
    def _pre_loop_hook(self, params=None):
        self.yelp_api_key = params.get('yelp_api_key')
        self.headers = {'Authorization': f'Bearer {self.yelp_api_key}'}
        self.request_timeout = params.get('request_timeout', 5)  # Default timeout set to 5 seconds

    def _execute(self, params=None):
        location = self.consumers['location_input'].next()
        response = requests.get(
            'https://api.yelp.com/v3/businesses/search',
            headers=self.headers,
            params={'location': location, 'categories': 'restaurants'},
            timeout=self.request_timeout  # Added timeout to the request
        )
        self.producers['restaurant_data'].produce(response.json())

class FaissIndexer(AbstractNode):
    def _pre_loop_hook(self, params=None):
        self.index = FaissIndex(params.get('index_path'))

    def _execute(self, params=None):
        data = self.consumers['restaurant_data'].next()
        enriched_data = self.index.enrich(data)
        self.producers['enriched_data'].produce(enriched_data)

class LLMRecommender(AbstractNode):
    def _pre_loop_hook(self, params=None):
        self.llm = OpenAICompletion()

    def _execute(self, params=None):
        prompt = self.consumers['enriched_data'].next()
        response = self.llm.complete(prompt)
        self.producers['recommendations'].produce(response)
