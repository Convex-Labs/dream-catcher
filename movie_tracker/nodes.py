from aineko.core.node import AbstractNode
from typing import Optional
import os
import requests

# Define your nodes here

class MovieFetcherNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Fetch new movie releases from an external API
        api_key = os.getenv('MOVIE_DB_API_KEY')
        response = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}', timeout=10)
        if response.status_code == 200:
            new_movies = response.json().get('results', [])
            self.producers['new_movies'].produce(new_movies)
        else:
            self.log(f'Failed to fetch new movies: {response.status_code}', level='error')

class RecommendationEngineNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Generate movie recommendations based on user preferences
        user_preferences = self.consumers['user_preferences'].consume()
        new_movies = self.consumers['new_movies'].consume()
        if user_preferences and new_movies:
            recommended_movies = [movie for movie in new_movies if self.match_preferences(movie, user_preferences)]
            self.producers['recommended_movies'].produce(recommended_movies)

    def match_preferences(self, movie, preferences):
        # Logic to match user preferences with movie attributes
        return all(pref in movie['genre_ids'] for pref in preferences['preferred_genres'])