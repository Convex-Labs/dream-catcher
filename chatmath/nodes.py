from aineko.core.node import AbstractNode
from typing import Optional
import openai
import ast

openai.api_key = 'your-openai-api-key'

# Define a node that interacts with ChatGPT

class ChatGPTNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        prompt = self.consumers['input_prompt'].next()
        if prompt:
            response = openai.Completion.create(
                engine='davinci',
                prompt=prompt,
                max_tokens=150
            )
            self.producers['chatgpt_response'].produce(response.choices[0].text)

# Define a node that performs a mathematical operation

class MathNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        math_expression = self.consumers['math_expression'].next()
        if math_expression:
            try:
                # Use ast.literal_eval for safe evaluation of the expression
                result = ast.literal_eval(math_expression)
            except Exception as e:
                result = str(e)
            self.producers['math_result'].produce(result)
