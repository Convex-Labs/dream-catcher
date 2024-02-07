from aineko.core.node import AbstractNode


class ChatGPTNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.openai_api_key = params.get('openai_api_key')

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        prompt = self.consumers['input_prompt'].next()
        if prompt:
            response = self.query_chatgpt(prompt)
            self.producers['gpt_response'].produce(response)

    def query_chatgpt(self, prompt):
        """Query ChatGPT with the given prompt."""
        import openai
        openai.api_key = self.openai_api_key
        return openai.Completion.create(
            engine='davinci',
            prompt=prompt,
            max_tokens=150
        )
