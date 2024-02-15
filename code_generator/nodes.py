from aineko.core.node import AbstractNode


class CodeGeneratorNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        self.template = params.get('template', '')

    def _execute(self, params=None):
        user_prompt = self.consumers['user_prompt'].next()
        code = self.template.format(**user_prompt)
        self.producers['generated_code'].produce(code)
