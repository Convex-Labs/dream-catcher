from aineko.core.node import AbstractNode
from typing import Optional
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

class QuoteGeneratorNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        prompt = 'Give me an inspirational quote.'
        response = openai.Completion.create(
            engine='davinci',
            prompt=prompt,
            max_tokens=60
        )
        quote = response.choices[0].text.strip()
        self.producers['inspirational_quote'].produce(quote)
