from aineko.core.node import AbstractNode
from typing import Optional
import requests
import os

# Define your nodes here

class MovieFetcherNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.api_key = os.getenv('MOVIE_DB_API_KEY')
        self.base_url = 'https://api.themoviedb.org/3'
        self.request_timeout = params.get('request_timeout', 10)  # Default timeout set to 10 seconds

    def _execute(self, params: Optional[dict] = None) -> None:
        try:
            response = requests.get(f'{self.base_url}/movie/now_playing', params={'api_key': self.api_key}, timeout=self.request_timeout)
            if response.status_code == 200:
                movies = response.json().get('results', [])
                self.producers['new_movies'].produce(movies)
        except requests.exceptions.RequestException as e:
            self.log(f'Request failed: {e}', level='error')


class RecommendationEngineNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        user_preferences = self.consumers['user_preferences'].consume()
        new_movies = self.consumers['new_movies'].consume()
        if user_preferences and new_movies:
            recommended_movies = self.filter_movies(new_movies, user_preferences)
            self.producers['movie_recommendations'].produce(recommended_movies)

    def filter_movies(self, movies, preferences):
        # Implement filtering logic based on preferences
        return [movie for movie in movies if self.match_preferences(movie, preferences)]

    def match_preferences(self, movie, preferences):
        # Check if the movie matches the user's preferences
        return all(movie.get(preference) == value for preference, value in preferences.items())