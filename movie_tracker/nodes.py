from aineko.core.node import AbstractNode
import requests
import json
from typing import Optional

class MovieFetcherNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        api_key = params.get('api_key')
        url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1'
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                movies = response.json().get('results', [])
                self.producers['new_movies'].produce(movies)
            else:
                self.log(f'Failed to fetch movies: {response.status_code}', level='error')
        except requests.Timeout:
            self.log('Request to the movie database API timed out', level='error')
        except requests.RequestException as e:
            self.log(f'Request to the movie database API failed: {e}', level='error')

class RecommendationEngineNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        user_preferences = params.get('user_preferences')
        movies = self.consumers['new_movies'].next()
        recommended_movies = []
        for movie in movies:
            if self._match_preferences(movie, user_preferences):
                recommended_movies.append(movie)
        self.producers['recommended_movies'].produce(recommended_movies)

    def _match_preferences(self, movie, preferences):
        for key, value in preferences.items():
            if movie.get(key) != value:
                return False
        return True