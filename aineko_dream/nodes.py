from aineko.core.node import AbstractNode
import os
import openai
from typing import Optional

openai.api_key = os.getenv('OPENAI_API_KEY')


class GitHubDocFetcher(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.repo = params.get('repo')
        self.file_path = params.get('file_path')
        self.document = ''
        # Fetch initial document
        self._fetch_document()

    def _execute(self, params: Optional[dict] = None) -> None:
        # Check for updates and fetch document
        self._fetch_document()

    def _fetch_document(self):
        # Simulate fetching document from GitHub
        with open(self.file_path, 'r') as file:
            self.document = file.read()
        self.producers['document'].produce(self.document)


class LLMQueryNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        prompt = self.consumers['prompt'].next()
        response = openai.Completion.create(
            engine='davinci',
            prompt=prompt,
            max_tokens=150
        )
        self.producers['response'].produce(response.choices[0].text)


class QualityAssuranceNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        response = self.consumers['response'].next()
        # Simulate quality assurance check
        if 'error' not in response:
            self.producers['final_output'].produce(response)
        else:
            self.producers['prompt'].produce('Please fix the following error: ' + response)
