from aineko.core.node import AbstractNode


class CodeGeneratorNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        self.template = params.get('template', '')

    def _execute(self, params=None):
        prompt_message = self.consumers['user_prompt'].next()
        code = self.template.format(**prompt_message)
        self.producers['generated_code'].produce(code)
