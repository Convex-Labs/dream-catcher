from aineko.core.node import AbstractNode
from typing import Optional
import openai

openai.api_key = 'your-openai-api-key'

# Define your nodes here

class MathChatNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None):
        self.prompt = params.get('prompt', 'Solve the following math problem: ')

    def _execute(self, params: Optional[dict] = None):
        math_problem = self.consumers['math_problems'].next()
        if math_problem:
            response = openai.Completion.create(
                engine='davinci',
                prompt=self.prompt + math_problem,
                max_tokens=150
            )
            self.producers['math_solutions'].produce(response.choices[0].text)
