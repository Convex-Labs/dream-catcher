from aineko.core.node import AbstractNode
from typing import Optional
import openai
import ast

openai.api_key = 'your-api-key'

# Define your nodes here
class ChatGPTNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        prompt = self.consumers['input_prompt'].next()
        if prompt:
            response = openai.Completion.create(
                engine='davinci',
                prompt=prompt,
                max_tokens=150
            )
            self.producers['gpt_output'].produce(response.choices[0].text)

class MathNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        expression = self.consumers['math_expression'].next()
        if expression:
            try:
                # Use ast.literal_eval for safe evaluation
                result = ast.literal_eval(expression)
                self.producers['math_output'].produce(result)
            except (ValueError, SyntaxError):
                self.log('Invalid math expression', level='error')
