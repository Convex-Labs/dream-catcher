from aineko.core.node import AbstractNode
from typing import Optional
import requests
from sqlalchemy import create_engine


class GitHubCrawlerNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None):
        self.github_api_url = 'https://api.github.com'
        self.db_engine = create_engine(params['database_url'])
        self.request_timeout = params.get('request_timeout', 10)  # Default timeout set to 10 seconds

    def _execute(self, params: Optional[dict] = None):
        users = requests.get(f'{self.github_api_url}/users', timeout=self.request_timeout).json()
        projects = requests.get(f'{self.github_api_url}/repositories', timeout=self.request_timeout).json()

        with self.db_engine.connect() as connection:
            for user in users:
                connection.execute(
                    """INSERT INTO users (id, login, url) VALUES (:id, :login, :url) ON CONFLICT (id) DO NOTHING""",
                    id=user['id'], login=user['login'], url=user['html_url']
                )
            for project in projects:
                connection.execute(
                    """INSERT INTO projects (id, name, owner_id) VALUES (:id, :name, :owner_id) ON CONFLICT (id) DO NOTHING""",
                    id=project['id'], name=project['name'], owner_id=project['owner']['id']
                )
