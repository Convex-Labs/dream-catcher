from aineko.core.node import AbstractNode
import secrets


class SurpriseNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        self.surprises = [
            'A virtual trip to Paris!',
            'A mystery novel e-book!',
            'A digital painting lesson!',
            'An online cooking class!',
            'A personalized workout plan!'
        ]

    def _execute(self, params=None):
        surprise_index = secrets.randbelow(len(self.surprises))
        surprise = self.surprises[surprise_index]
        self.outputs['surprise_output'].write(surprise)
        self.log(f'Generated surprise: {surprise}', level='info')
